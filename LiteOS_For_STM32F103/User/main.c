/* Includes ----------------------------------------------------------------*/
// Huawei LiteOS头文件
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "los_base.h"
#include "los_config.h"
#include "los_typedef.h"
#include "los_hwi.h"
#include "los_task.ph"
#include "los_sem.h"
#include "los_event.h"
#include "los_memory.h"
#include "los_queue.ph"
// STM32硬件相关头文件
#include "stm32f10x.h"
#include "bsp_led.h"
#include "bsp_usart.h"
#include "lcd.h"
#include "key.h"

UINT32 handle_queue;


void Delay(__IO u32 nCount);
#define SOFT_DELAY Delay(0x0FFFFF);
UINT32 g_TestTskHandle;
UINT32 g_QueueWriteTskHandle;
UINT32 g_QueueReadTskHandle;


void Delay(__IO uint32_t nCount) //简单延时
{
	for(; nCount != 0; nCount--);
}
void hardware_init(void)
{
	LED_GPIO_Config();
	USART_Config();
	KEY_Init();
//	delay_init();	    	 //延时函数初始化	 
//	LCD_Init();
//	LCD_Clear(BLUE);
}
VOID task1(void)
{
	UINT32 uwRet = LOS_OK;
	UINT32 count=0;
	while(1)
	{
		count++;
		printf("this is task 1,count is %d\r\n",count);
		LED0_TOGGLE;//LED0翻转
		uwRet = LOS_TaskDelay(1000);//系统延时1S
		if(uwRet !=LOS_OK)
		return;
	} 
}
UINT32 creat_task1(void)
{
	UINT32 uwRet = LOS_OK;
	TSK_INIT_PARAM_S task_init_param;
	task_init_param.usTaskPrio = 10;//任务优先级，0最高
	task_init_param.pcName = "LED_BLINK";//任务名称
	task_init_param.pfnTaskEntry = (TSK_ENTRY_FUNC)task1;//任务入口函数
	task_init_param.uwStackSize = LOSCFG_BASE_CORE_TSK_DEFAULT_STACK_SIZE;//任务堆栈大小
	task_init_param.uwResved = LOS_TASK_STATUS_DETACHED;
	uwRet = LOS_TaskCreate(&g_TestTskHandle,&task_init_param);//创建任务
	if(uwRet !=LOS_OK)
	{
		return uwRet;
	}
	return uwRet;
}


VOID QueueWrite(void)
{
	UINT32 uwRet = LOS_OK;
	UINT32 queueMsg1 = 1;
	UINT32 queueMsg2 = 2;
	UINT32 keyVal;
	
	while(1)
	{
		keyVal = KEY_Scan(0);
		
		if(KEY0_PRES == keyVal)
		{
			uwRet = LOS_QueueWrite(handle_queue, &queueMsg1, sizeof(queueMsg1), 0);
			if(LOS_OK == uwRet)
			{
				printf("成功写入队列数据：1\n");
			}
		}
		if(WKUP_PRES == keyVal)
		{
			uwRet = LOS_QueueWrite(handle_queue, &queueMsg2, sizeof(queueMsg2), 0);
			if(LOS_OK == uwRet)
			{
				printf("成功写入队列数据：2\n");
			}
		}
		LOS_TaskDelay(20);
	} 
}
UINT32 QueueWrite_task(void)
{
	UINT32 uwRet = LOS_OK;
	TSK_INIT_PARAM_S task_init_param;
	task_init_param.usTaskPrio = 4;//任务优先级，0最高
	task_init_param.pcName = "QueueWrite";//任务名称
	task_init_param.pfnTaskEntry = (TSK_ENTRY_FUNC)QueueWrite;//任务入口函数
	task_init_param.uwStackSize = LOSCFG_BASE_CORE_TSK_DEFAULT_STACK_SIZE;//任务堆栈大小
	task_init_param.uwResved = LOS_TASK_STATUS_DETACHED;
	uwRet = LOS_TaskCreate(&g_QueueWriteTskHandle,&task_init_param);//创建任务
	if(uwRet !=LOS_OK)
	{
		return uwRet;
	}
	printf("QueueWrite任务创建成功\n");
	return uwRet;
}

VOID QueueRead(void)
{
	UINT32 uwRet = LOS_OK;
	UINT32 read = 0;
	while(1)
	{
		uwRet = LOS_QueueRead(handle_queue, &read,  sizeof(read), LOS_WAIT_FOREVER);
		if(LOS_OK == uwRet)
		{
			printf("成功读取队列数据:%d\n", *(UINT32 *)read);
		}
		else
		{
			printf("数据读取错误:%d\n", uwRet);
		}
		
	} 
}
UINT32 QueueRead_task(void)
{
	UINT32 uwRet = LOS_OK;
	TSK_INIT_PARAM_S task_init_param;
	task_init_param.usTaskPrio = 5;//任务优先级，0最高
	task_init_param.pcName = "QueueRead";//任务名称
	task_init_param.pfnTaskEntry = (TSK_ENTRY_FUNC)QueueRead;//任务入口函数
	task_init_param.uwStackSize = LOSCFG_BASE_CORE_TSK_DEFAULT_STACK_SIZE;//任务堆栈大小
	task_init_param.uwResved = LOS_TASK_STATUS_DETACHED;
	uwRet = LOS_TaskCreate(&g_QueueReadTskHandle,&task_init_param);//创建任务
	if(uwRet !=LOS_OK)
	{
		return uwRet;
	}
	printf("QueueRead任务创建成功\n");
	return uwRet;
}

UINT32 osAppInit(void)
{
	UINT32 uwRet = 0;
	hardware_init();
	LED0_ON;
	SOFT_DELAY;
	printf("Powered by LiteOS\r\n");
	
	uwRet = LOS_QueueCreate("TEST_QUEUE", 10, &handle_queue, 0, 16);
	if(LOS_OK == uwRet)
	{
		printf("队列创建成功");
	}
	
	uwRet = QueueWrite_task();
	if(uwRet !=LOS_OK)
	{
		return uwRet;
	}
	
	uwRet = QueueRead_task();
	if(uwRet !=LOS_OK)
	{
		return uwRet;
	}


	return LOS_OK;
}
/*********************************************END OF FILE**********************/
