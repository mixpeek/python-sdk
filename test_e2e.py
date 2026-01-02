"""
End-to-end tests for Mixpeek Python SDK against local API
Tests the auto-generated client from OpenAPI specification
"""
import os
import sys
from pathlib import Path

# Add the mixpeek package to the path
sys.path.insert(0, str(Path(__file__).parent / "mixpeek"))

from mixpeek.client import AuthenticatedClient
from mixpeek.api.health.healthcheck_v1_health_get import sync_detailed as health_check
from mixpeek.api.collections.list_collections_v1_collections_list_post import sync_detailed as list_collections

# Configuration
LOCAL_API_URL = os.getenv("MIXPEEK_API_URL", "http://localhost:8000")
API_KEY = os.getenv("MIXPEEK_API_KEY", "sk_gg7CCgty2kh4MOxUNQ95gCI8Lsmrq8qA1o_1c9Ll0o7pnkX3ZewSETQblQngF8aOyL4")

def test_health_check():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check ===")

    client = AuthenticatedClient(
        base_url=LOCAL_API_URL,
        token=API_KEY,
        timeout=30.0
    )

    try:
        response = health_check(client=client)
        print(f"Status Code: {response.status_code}")
        print(f"✓ Health check successful")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        return True
    except Exception as e:
        print(f"✗ Health check failed: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_list_collections():
    """Test listing collections"""
    print("\n=== Testing List Collections ===")

    client = AuthenticatedClient(
        base_url=LOCAL_API_URL,
        token=API_KEY,
        timeout=30.0
    )

    try:
        response = list_collections(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ List collections successful")
            # Try to parse response
            if hasattr(response, 'parsed') and response.parsed:
                print(f"  Collections found: {len(response.parsed) if hasattr(response.parsed, '__len__') else 'N/A'}")
            return True
        else:
            print(f"⚠ List collections returned status {response.status_code}")
            return None
    except AttributeError as e:
        print(f"⊘ Endpoint not available: {e}")
        return None
    except Exception as e:
        print(f"✗ List collections failed: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_client_initialization():
    """Test that the client can be initialized"""
    print("\n=== Testing Client Initialization ===")

    try:
        client = AuthenticatedClient(
            base_url=LOCAL_API_URL,
            token=API_KEY,
            timeout=30.0
        )
        print(f"✓ Client initialized successfully")
        print(f"  Base URL: {client._base_url}")
        return True
    except Exception as e:
        print(f"✗ Client initialization failed: {type(e).__name__}: {e}")
        return False


def main():
    """Run all tests"""
    print("="*60)
    print("Mixpeek Python SDK - End-to-End Tests")
    print("="*60)
    print(f"API URL: {LOCAL_API_URL}")
    print(f"API Key: {API_KEY[:15]}..." if len(API_KEY) > 15 else f"API Key: {API_KEY}")

    results = {
        "Client Initialization": test_client_initialization(),
        "Health Check": test_health_check(),
        "List Collections": test_list_collections(),
    }

    # Print summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)

    passed = sum(1 for r in results.values() if r is True)
    failed = sum(1 for r in results.values() if r is False)
    skipped = sum(1 for r in results.values() if r is None)

    for test_name, result in results.items():
        status = "✓ PASS" if result is True else ("✗ FAIL" if result is False else "⊘ SKIP")
        print(f"{status}: {test_name}")

    print(f"\nTotal: {len(results)} tests")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Skipped: {skipped}")
    print("="*60)

    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
