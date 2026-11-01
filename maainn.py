import asyncio

async def fetch_data(param):
    print(f"Started {param}")

    if param == 2:
        raise ValueError("Error in coroutine 2")

    await asyncio.sleep(param)

    print(f"Completed {param}")
    return f"Result {param}"


async def main():
    coroutines = [fetch_data(i) for i in range(1, 4)]

    try:
        results = await asyncio.gather(*coroutines,return_exceptions=True)
        print("Results:", results)

    except ValueError as e:
        print("Caught exception:", e)

    await asyncio.sleep(4)
    print("Main completed")

asyncio.run(main())
