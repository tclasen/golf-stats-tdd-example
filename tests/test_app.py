from typing import Any

import schemathesis

from example import app

schemathesis.fixups.install()

schema = schemathesis.from_asgi("/openapi.json", app)


@schema.parametrize()  # type: ignore
def test_api(case: Any) -> None:
    response = case.call_asgi()
    case.validate_response(response)
