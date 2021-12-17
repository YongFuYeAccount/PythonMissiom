/**
  ******************************************************************************
  * @file    CommonFx.c
  * @author  Chen Qi����
  * @version V1.6
  * @date    2017-4-24
  * @brief   ���ú���.c�ļ�
  ******************************************************************************
  * @attention
  *
  * ����������
  * 1.���ӳٺ���
  * 2.�׳˺���
  * 3.����ֵ����
  * 4.���������ֽ�
  * 5.ϵͳ�δ�ʱ����ʼ��
  * 6.us�ӳٳ���
  *	7.���Ļ�ȡ����
  * 8.PID����
  *	9.����ƽ��������
  ******************************************************************************
  */

#include "CommonFx.h"

static __IO u32 TimingDelay;

/**
  * @brief  �򵥵���ʱ����
  * @param  __IO uint32_t nCount
  * @retval ��
  */
void EasyDelay(__IO uint32_t nCount)	 //�򵥵���ʱ����
{
	for(; nCount != 0; nCount--);        //10000~(0.0016s-0.00175s)
}

/**
  * @brief  �׳˺���
  * @param  unsigned char m,unsigned char n(����m^n)
  * @retval unsigned long
  */
unsigned long Pow(unsigned char m,unsigned char n)
{
	unsigned long result=1;
	while(n--)result*=m;
	return result;
}

/**
  * @brief  ����ֵ����
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
  * @brief  ���������ֽ�
  * @param  u8* m,u8 *n
  * @retval ��
  */
void U8change(u8* m,u8* n)
{
	u8 k;
	k=*m;
	*m=*n;
	*n=k;
}

/************************************************************
  ��ʹ��ϵͳʱ���Դ��δ�ʱ�������ж�c�ļ����������´���
  #include "stm32f10x_it.h"��ӣ�
  extern void TimingDelay_Decrement(void);//�����ⲿ��������
  void SysTick_Handler(void)���������ӣ�
  TimingDelay_Decrement();
*************************************************************/

/**
  * @brief  ����ϵͳ�δ�ʱ�� SysTick
  * @param  ��
  * @retval ��
  */
void SysTick_Init(void)
{
	/*
	 ***************************************
	 * SystemFrequency/1000    1ms�ж�һ��
	 * SystemFrequency/100000	 10us�ж�һ��
	 * SystemFrequency/1000000 1us�ж�һ��
	 ***************************************
	 */
	if (SysTick_Config(SystemCoreClock/1000000))	//ST3.5.0��汾ʹ��(����72000000/1000000=72��ʱ�����ڲ���һ���ж�)
	{
		/* Capture error */
		while (1);
	}
	SysTick->CTRL &= ~ SysTick_CTRL_ENABLE_Msk;   //�رյδ�ʱ��
}

/**
  * @brief   us��ʱ����,1usΪһ����λ
  * @param   __IO u32 nTime:Delay_us(1)��ʵ�ֵ���ʱΪ1*1us=1us
  * @retval  ��
  */
void Delay_us(__IO u32 nTime)
{
	TimingDelay = nTime;
	SysTick->CTRL |=  SysTick_CTRL_ENABLE_Msk;   //ʹ�ܵδ�ʱ��
	while(TimingDelay != 0);
}

/**
  * @brief  ��ȡ���ĳ���
  * @param  ��
  * @retval ��
  ******************************************************
  * @attention  ��SysTick�жϺ���SysTick_Handler()����
  */
void TimingDelay_Decrement(void)
{
	if (TimingDelay != 0x00)
	{
		TimingDelay--;
	}
}

/**
  * @brief  PID����
  * @param  ��
  * @retval ��
	* @illustration U(k)=KP*E(k)+KI*I(k)+KD*[E(k)-E(k-1)]
  */
void PID_Operation(PID_ValueStr* PID)
{
	int Temp[3] = {0};   																	//�м���ʱ����(����Temp[i]�ֱ�ΪP��I��D����ֵ)
	int iTemp;																						//�м���ʱ������(��������)
	if(PID->iCurVal < PID->iSetVal + PID->dSCVal ||\
		 PID->iCurVal > PID->iSetVal - PID->dSCVal)					//ʵ��ֵ�����趨ֵ��������Χ����ʱ�������Ҫ�ı�
	{
		if(PID->iSetVal - PID->iCurVal > (int)PID->MOUT_Ek)	//ƫ��ֵ����MOUT_Ek
			PID->iPriVal = PID->OUT_MAX;                			//���޷�ֵ���
		else if(PID->iCurVal - PID->iSetVal > (int)PID->MOUT_Ek)
			PID->iPriVal = -PID->OUT_MAX;                			//�����޷�ֵ���
		else																				 	  		//ƫ��ֵС��MOUT_Ek
		{
			Temp[0] = PID->iSetVal - PID->iCurVal;    				//����E(k)
			//k++
			PID->liEkVal[2] += Temp[0];												//I(k)���ִ洢
      PID->liEkVal[1] = PID->liEkVal[0];								//E'(k-1)=E'(k)
      PID->liEkVal[0] = Temp[0];												//E'(k)=E(k) E(k)Ϊ��ֵ
			if(PID->liEkVal[2] > 1500000) PID->liEkVal[2] = 1500000;
			if(PID->liEkVal[2] < -1500000) PID->liEkVal[2] = -1500000;
																												//�����޷�
			Temp[2] = PID->liEkVal[0] - PID->liEkVal[1];			//Temp[2]=E(k)-E(k-1)
			Temp[0] = (int)(PID->uKP_Coe * Temp[0]);      		//Temp[0]=KP*E(k)
      Temp[1] = (int)(PID->uKI_Coe * PID->liEkVal[2]);	//Temp[1]=KI*I(k)
      Temp[2] = (int)(PID->uKD_Coe * Temp[2]);        	//Temp[2]=KD*[E(k)-E(k-1)]
			iTemp=Temp[0]+Temp[1]+Temp[2];
			if(iTemp>0)																				//������Ϊ��
			{
				if(iTemp<=(int)PID->OUT_MAX)										//δ�������޷�ֵ���������ֵ
					PID->iPriVal = iTemp;
				else																						//����������޷�ֵ
					PID->iPriVal = PID->OUT_MAX;
			}
			else																							//������Ϊ��
			{
				if(iTemp>=(int)(-PID->OUT_MAX))									//δ�������޷�ֵ���������ֵ
					PID->iPriVal = iTemp;
				else																						//������������޷�ֵ
					PID->iPriVal = -PID->OUT_MAX;
			}
		}
	}
}

/**
  * @brief  ����ƽ��������
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
  * @brief  ʮ����ת������
  * @param  u16 x(��ת������)    u8* p(ת���������飩 u8 i(���鳤��)
  * @retval ��
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
  * @brief  ������תʮ����
  * @param   u8* p(ת���������飩 u8 i(���鳤��)
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
