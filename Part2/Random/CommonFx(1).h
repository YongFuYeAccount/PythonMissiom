/**
  ******************************************************************************
  * @file    CommonFx.h
  * @author  Chen Qi zero
  * @version V1.5
  * @date    2016-11-29
  * @brief   常用函数头文件
  ******************************************************************************
  * @attention
  *
  * 函数包括：
	* 1.简单延迟函数 
  * 2.阶乘函数
  * 3.系统滴答定时器初始化
  * 4.us延迟程序
  *	5.节拍获取程序
	* 6.PID运算
	*
  ******************************************************************************
  */ 
	
#ifndef __CommonFx_H
#define __CommonFx_H
#include "stm32f10x.h"

#include <math.h>

//IO操作宏定义
#define BITBAND(addr, bitnum) ((addr & 0xF0000000)+0x2000000+((addr &0xFFFFF)<<5)+(bitnum<<2)) 
#define MEM_ADDR(addr)  *((volatile unsigned long  *)(addr)) 
#define BIT_ADDR(addr, bitnum)   MEM_ADDR(BITBAND(addr, bitnum))  

//IO地址映射
#define GPIOA_ODR_Addr    (GPIOA_BASE+12) //0x4001080C 
#define GPIOB_ODR_Addr    (GPIOB_BASE+12) //0x40010C0C 
#define GPIOC_ODR_Addr    (GPIOC_BASE+12) //0x4001100C 
#define GPIOD_ODR_Addr    (GPIOD_BASE+12) //0x4001140C 
#define GPIOE_ODR_Addr    (GPIOE_BASE+12) //0x4001180C 
#define GPIOF_ODR_Addr    (GPIOF_BASE+12) //0x40011A0C    
#define GPIOG_ODR_Addr    (GPIOG_BASE+12) //0x40011E0C    

#define GPIOA_IDR_Addr    (GPIOA_BASE+8) //0x40010808 
#define GPIOB_IDR_Addr    (GPIOB_BASE+8) //0x40010C08 
#define GPIOC_IDR_Addr    (GPIOC_BASE+8) //0x40011008 
#define GPIOD_IDR_Addr    (GPIOD_BASE+8) //0x40011408 
#define GPIOE_IDR_Addr    (GPIOE_BASE+8) //0x40011808 
#define GPIOF_IDR_Addr    (GPIOF_BASE+8) //0x40011A08 
#define GPIOG_IDR_Addr    (GPIOG_BASE+8) //0x40011E08 

#define PAout(n)   BIT_ADDR(GPIOA_ODR_Addr,n)  //PA输出
#define PAin(n)    BIT_ADDR(GPIOA_IDR_Addr,n)  //PA输入

#define PBout(n)   BIT_ADDR(GPIOB_ODR_Addr,n)  //PB输出
#define PBin(n)    BIT_ADDR(GPIOB_IDR_Addr,n)  //PB输入

#define PCout(n)   BIT_ADDR(GPIOC_ODR_Addr,n)  //PC输出
#define PCin(n)    BIT_ADDR(GPIOC_IDR_Addr,n)  //PC输入

#define PDout(n)   BIT_ADDR(GPIOD_ODR_Addr,n)  //PD输出
#define PDin(n)    BIT_ADDR(GPIOD_IDR_Addr,n)  //PD输入

#define PEout(n)   BIT_ADDR(GPIOE_ODR_Addr,n)  //PE输出
#define PEin(n)    BIT_ADDR(GPIOE_IDR_Addr,n)  //PE输入

#define PFout(n)   BIT_ADDR(GPIOF_ODR_Addr,n)  //PF输出
#define PFin(n)    BIT_ADDR(GPIOF_IDR_Addr,n)  //PF输入

#define PGout(n)   BIT_ADDR(GPIOG_ODR_Addr,n)  //PG输出
#define PGin(n)    BIT_ADDR(GPIOG_IDR_Addr,n)  //PG输入

//自定义类型结构体 PID参数
typedef struct PID_Value
{
    int liEkVal[3];         		  //差值保存，给定和反馈的差值
    float  uKP_Coe;             	//比例系数
    float  uKI_Coe;             	//积分常数
    float  uKD_Coe;             	//微分常数
		u32 OUT_MAX;									//上限幅值输出
		u32 MOUT_Ek;									//确定上限幅值输出的差值标准(必须满足MOUT_Ek>dSCVal否则无法上限幅值输出)
		int iPriVal;            		  //(上一时刻)输出值(值在-OUT_MAX~OUT_MAX间)
    int iSetVal;            			//设定值
    int iCurVal;             			//实际值
	  u16 dSCVal;										//允许实际值与设定值的误差
}PID_ValueStr;

void EasyDelay(__IO u32 nCount); 
unsigned long Pow(unsigned char,unsigned char);
void SysTick_Init(void);
void Delay_us(__IO u32 nTime);
void TimingDelay_Decrement(void);
void PID_Operation(PID_ValueStr*);
float Q_sqrt(float number);
void Dec2Bin (u16 x,u8* p,u8 i);
u16 Bin2Dec(u8* p,u8 i);
#endif
/********************************END OF FILE***********************************/
