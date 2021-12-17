/**
  ******************************************************************************
  * @file    CommonFx.h
  * @author  Chen Qi zero
  * @version V1.5
  * @date    2016-11-29
  * @brief   ���ú���ͷ�ļ�
  ******************************************************************************
  * @attention
  *
  * ����������
	* 1.���ӳٺ��� 
  * 2.�׳˺���
  * 3.ϵͳ�δ�ʱ����ʼ��
  * 4.us�ӳٳ���
  *	5.���Ļ�ȡ����
	* 6.PID����
	*
  ******************************************************************************
  */ 
	
#ifndef __CommonFx_H
#define __CommonFx_H
#include "stm32f10x.h"

#include <math.h>

//IO�����궨��
#define BITBAND(addr, bitnum) ((addr & 0xF0000000)+0x2000000+((addr &0xFFFFF)<<5)+(bitnum<<2)) 
#define MEM_ADDR(addr)  *((volatile unsigned long  *)(addr)) 
#define BIT_ADDR(addr, bitnum)   MEM_ADDR(BITBAND(addr, bitnum))  

//IO��ַӳ��
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

#define PAout(n)   BIT_ADDR(GPIOA_ODR_Addr,n)  //PA���
#define PAin(n)    BIT_ADDR(GPIOA_IDR_Addr,n)  //PA����

#define PBout(n)   BIT_ADDR(GPIOB_ODR_Addr,n)  //PB���
#define PBin(n)    BIT_ADDR(GPIOB_IDR_Addr,n)  //PB����

#define PCout(n)   BIT_ADDR(GPIOC_ODR_Addr,n)  //PC���
#define PCin(n)    BIT_ADDR(GPIOC_IDR_Addr,n)  //PC����

#define PDout(n)   BIT_ADDR(GPIOD_ODR_Addr,n)  //PD���
#define PDin(n)    BIT_ADDR(GPIOD_IDR_Addr,n)  //PD����

#define PEout(n)   BIT_ADDR(GPIOE_ODR_Addr,n)  //PE���
#define PEin(n)    BIT_ADDR(GPIOE_IDR_Addr,n)  //PE����

#define PFout(n)   BIT_ADDR(GPIOF_ODR_Addr,n)  //PF���
#define PFin(n)    BIT_ADDR(GPIOF_IDR_Addr,n)  //PF����

#define PGout(n)   BIT_ADDR(GPIOG_ODR_Addr,n)  //PG���
#define PGin(n)    BIT_ADDR(GPIOG_IDR_Addr,n)  //PG����

//�Զ������ͽṹ�� PID����
typedef struct PID_Value
{
    int liEkVal[3];         		  //��ֵ���棬�����ͷ����Ĳ�ֵ
    float  uKP_Coe;             	//����ϵ��
    float  uKI_Coe;             	//���ֳ���
    float  uKD_Coe;             	//΢�ֳ���
		u32 OUT_MAX;									//���޷�ֵ���
		u32 MOUT_Ek;									//ȷ�����޷�ֵ����Ĳ�ֵ��׼(��������MOUT_Ek>dSCVal�����޷����޷�ֵ���)
		int iPriVal;            		  //(��һʱ��)���ֵ(ֵ��-OUT_MAX~OUT_MAX��)
    int iSetVal;            			//�趨ֵ
    int iCurVal;             			//ʵ��ֵ
	  u16 dSCVal;										//����ʵ��ֵ���趨ֵ�����
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
