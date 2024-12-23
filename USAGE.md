<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from mixpeek import Mixpeek
import os

with Mixpeek(
    bearer_auth=os.getenv("MIXPEEK_BEARER_AUTH", ""),
) as mixpeek:

    res = mixpeek.organizations.get()

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
        bearer_auth=os.getenv("MIXPEEK_BEARER_AUTH", ""),
    ) as mixpeek:

        res = await mixpeek.organizations.get_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->