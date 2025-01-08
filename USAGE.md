<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from mixpeek import Mixpeek
import os

with Mixpeek(
    token=os.getenv("MIXPEEK_TOKEN", ""),
) as mixpeek:

    res = mixpeek.health.check()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from mixpeek import Mixpeek
import os

async def main():
    async with Mixpeek(
        token=os.getenv("MIXPEEK_TOKEN", ""),
    ) as mixpeek:

        res = await mixpeek.health.check_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->