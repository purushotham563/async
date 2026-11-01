import time
import asyncio

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    tast1 = fetch_data(1)
    tast2=fetch_data(2)
    result1=await tast1
    print("Task 1 fully completed")
    result2 = await tast2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results =asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")