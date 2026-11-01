import time
import asyncio
def sync_function(test_param:str)->str:
    print("This is synchronous function")
    time.sleep(0.1)
    return f"Sync Result: {test_param}"
async def async_function(test_param:str)->str:
    print("This is asynchrnous function")
    await asyncio.sleep(0.1)
    return f"Async Result: {test_param}"
async def main():
    # corountine_obj=async_function("Test")
    # print(corountine_obj)
    # corountine_result=await corountine_obj
    # print(corountine_result)
    task=asyncio.create_task(async_function("Test"))
    print(task)
    task_result=await task
    print(task_result)
if __name__=="__main__":
    asyncio.run(main())
