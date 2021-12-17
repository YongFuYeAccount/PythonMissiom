/**
  ******************************************************************************
  * @file    CommonFx.c
  * @author  Chen Qi，零
  * @version V1.6
  * @date    2017-4-24
  * @brief   常用函数.c文件
  ******************************************************************************
  * @attention
  *
  * 函数包括：
  * 1.简单延迟函数
  * 2.阶乘函数
  * 3.绝对值函数
  * 4.交换两个字节
  * 5.系统滴答定时器初始化
  * 6.us延迟程序
  *	7.节拍获取程序
  * 8.PID运算
  *	9.快速平方根计算
  ******************************************************************************
  */

#include "CommonFx.h"

static __IO u32 TimingDelay;

/**
  * @brief  简单的延时函数
  * @param  __IO uint32_t nCount
  * @retval 无
  */
void EasyDelay(__IO uint32_t nCount)	 //简单的延时函数
{
	for(; nCount != 0; nCount--);        //10000~(0.0016s-0.00175s)
}

/**
  * @brief  阶乘函数
  * @param  unsigned char m,unsigned char n(返回m^n)
  * @retval unsigned long
  */
unsigned long Pow(unsigned char m,unsigned char n)
{
	unsigned long result=1;
	while(n--)result*=m;
	return result;
}

/**
  * @brief  绝对值函数
  * @param  long n
  * @retval unsigned long
  */
unsigned long Abs(long n)
{
	if(n>0)
		return n;
	else
		return -n;
}

/**
  * @brief  交换两个字节
  * @param  u8* m,u8 *n
  * @retval 无
  */
void U8change(u8* m,u8* n)
{
	u8 k;
	k=*m;
	*m=*n;
	*n=k;
}

/************************************************************
  如使用系统时钟自带滴答定时器需在中断c文件里增加如下代码
  #include "stm32f10x_it.h"后加：
  extern void TimingDelay_Decrement(void);//函数外部引用声明
  void SysTick_Handler(void)函数中增加：
  TimingDelay_Decrement();
*************************************************************/

/**
  * @brief  启动系统滴答定时器 SysTick
  * @param  无
  * @retval 无
  */
void SysTick_Init(void)
{
	/*
	 ***************************************
	 * SystemFrequency/1000    1ms中断一次
	 * SystemFrequency/100000	 10us中断一次
	 * SystemFrequency/1000000 1us中断一次
	 ***************************************
	 */
	if (SysTick_Config(SystemCoreClock/1000000))	//ST3.5.0库版本使用(经过72000000/1000000=72个时钟周期产生一次中断)
	{
		/* Capture error */
		while (1);
	}
	SysTick->CTRL &= ~ SysTick_CTRL_ENABLE_Msk;   //关闭滴答定时器
}

/**
  * @brief   us延时程序,1us为一个单位
  * @param   __IO u32 nTime:Delay_us(1)则实现的延时为1*1us=1us
  * @retval  无
  */
void Delay_us(__IO u32 nTime)
{
	TimingDelay = nTime;
	SysTick->CTRL |=  SysTick_CTRL_ENABLE_Msk;   //使能滴答定时器
	while(TimingDelay != 0);
}

/**
  * @brief  获取节拍程序
  * @param  无
  * @retval 无
  ******************************************************
  * @attention  在SysTick中断函数SysTick_Handler()调用
  */
void TimingDelay_Decrement(void)
{
	if (TimingDelay != 0x00)
	{
		TimingDelay--;
	}
}

/**
  * @brief  PID运算
  * @param  无
  * @retval 无
	* @illustration U(k)=KP*E(k)+KI*I(k)+KD*[E(k)-E(k-1)]
  */
void PID_Operation(PID_ValueStr* PID)
{
	int Temp[3] = {0};   																	//中间临时变量(最终Temp[i]分别为P、I、D计算值)
	int iTemp;																						//中间临时变量和(控制量和)
	if(PID->iCurVal < PID->iSetVal + PID->dSCVal ||\
		 PID->iCurVal > PID->iSetVal - PID->dSCVal)					//实际值不在设定值所允许误差范围，此时输出量需要改变
	{
		if(PID->iSetVal - PID->iCurVal > (int)PID->MOUT_Ek)	//偏差值大于MOUT_Ek
			PID->iPriVal = PID->OUT_MAX;                			//上限幅值输出
		else if(PID->iCurVal - PID->iSetVal > (int)PID->MOUT_Ek)
			PID->iPriVal = -PID->OUT_MAX;                			//负上限幅值输出
		else																				 	  		//偏差值小于MOUT_Ek
		{
			Temp[0] = PID->iSetVal - PID->iCurVal;    				//计算E(k)
			//k++
			PID->liEkVal[2] += Temp[0];												//I(k)积分存储
      PID->liEkVal[1] = PID->liEkVal[0];								//E'(k-1)=E'(k)
      PID->liEkVal[0] = Temp[0];												//E'(k)=E(k) E(k)为新值
			if(PID->liEkVal[2] > 1500000) PID->liEkVal[2] = 1500000;
			if(PID->liEkVal[2] < -1500000) PID->liEkVal[2] = -1500000;
																												//积分限幅
			Temp[2] = PID->liEkVal[0] - PID->liEkVal[1];			//Temp[2]=E(k)-E(k-1)
			Temp[0] = (int)(PID->uKP_Coe * Temp[0]);      		//Temp[0]=KP*E(k)
      Temp[1] = (int)(PID->uKI_Coe * PID->liEkVal[2]);	//Temp[1]=KI*I(k)
      Temp[2] = (int)(PID->uKD_Coe * Temp[2]);        	//Temp[2]=KD*[E(k)-E(k-1)]
			iTemp=Temp[0]+Temp[1]+Temp[2];
			if(iTemp>0)																				//控制量为正
			{
				if(iTemp<=(int)PID->OUT_MAX)										//未超出上限幅值则输出计算值
					PID->iPriVal = iTemp;
				else																						//否则输出上限幅值
					PID->iPriVal = PID->OUT_MAX;
			}
			else																							//控制量为负
			{
				if(iTemp>=(int)(-PID->OUT_MAX))									//未超出上限幅值则输出计算值
					PID->iPriVal = iTemp;
				else																						//否则输出负上限幅值
					PID->iPriVal = -PID->OUT_MAX;
			}
		}
	}
}

/**
  * @brief  快速平方根计算
  * @param  float number
  * @retval float
  */

float Q_sqrt(float number)
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;
	x2 = number * 0.5F;
	y = number;
	i = * ( long * ) & y;
	i = 0x5f3759df - ( i >> 1 );
	y = * ( float * ) & i;
	y = y * (threehalfs - ( x2 * y * y ) );
	y = y * (threehalfs - ( x2 * y * y ) );
	return 1.0/y;
}

/**
  * @brief  十进制转二进制
  * @param  u16 x(被转换的数)    u8* p(转换到的数组） u8 i(数组长度)
  * @retval 无
  */

  void Dec2Bin (u16 x,u8* p,u8 i)
{
    u16 temp;
    p+=i;
    while(--i>0)
    {
        temp = x >> 1;
        *--p = (x - (temp<<1));
        x>>=1;
    }
}

/**
  * @brief  二进制转十进制
  * @param   u8* p(转换到的数组） u8 i(数组长度)
  * @retval u16
  */

u16 Bin2Dec(u8* p,u8 i)
{
    u16 dec=0;
    p+=i;
    while(--i>0)
        dec += *--p<<(7-i);
    return dec;
}
/********************************END OF FILE***********************************/
