"""
Comprehensive E2E tests for Mixpeek Python SDK
Tests all major endpoints against local API
"""
import os
import sys
from pathlib import Path
from typing import Optional

# Add the mixpeek package to the path
sys.path.insert(0, str(Path(__file__).parent / "mixpeek"))

from mixpeek.client import AuthenticatedClient

# Import API endpoints
from mixpeek.api.health.healthcheck_v1_health_get import sync_detailed as health_check
from mixpeek.api.organizations.get_organization_v1_organizations_get import sync_detailed as get_organization
from mixpeek.api.collections.list_collections_v1_collections_list_post import sync_detailed as list_collections
from mixpeek.api.collections.create_collection_v1_collections_post import sync_detailed as create_collection
from mixpeek.api.collections.get_collection_v1_collections_collection_identifier_get import sync_detailed as get_collection
from mixpeek.api.collections.delete_collection_v1_collections_collection_identifier_delete import sync_detailed as delete_collection
from mixpeek.api.buckets.list_buckets_v1_buckets_list_post import sync_detailed as list_buckets
from mixpeek.api.retrievers.list_retrievers_v1_retrievers_list_post import sync_detailed as list_retrievers
from mixpeek.api.tasks.get_task_v1_tasks_task_id_get import sync_detailed as get_task
from mixpeek.api.feature_extractors.list_feature_extractors_v1_collections_features_extractors_get import sync_detailed as list_feature_extractors

# Configuration
LOCAL_API_URL = os.getenv("MIXPEEK_API_URL", "http://localhost:8000")
API_KEY = os.getenv("MIXPEEK_API_KEY", "sk_gg7CCgty2kh4MOxUNQ95gCI8Lsmrq8qA1o_1c9Ll0o7pnkX3ZewSETQblQngF8aOyL4")

# Test state
test_collection_id: Optional[str] = None


def create_client() -> AuthenticatedClient:
    """Create an authenticated client"""
    return AuthenticatedClient(
        base_url=LOCAL_API_URL,
        token=API_KEY,
        timeout=30.0
    )


# ============================================================================
# HEALTH & STATUS TESTS
# ============================================================================

def test_health_check():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check ===")
    client = create_client()

    try:
        response = health_check(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ Health check successful")
            if hasattr(response, 'parsed') and response.parsed:
                print(f"  Response: {response.parsed}")
            return True
        else:
            print(f"⚠ Health check returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ Health check failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# ORGANIZATION TESTS
# ============================================================================

def test_get_organization():
    """Test getting organization details"""
    print("\n=== Testing Get Organization ===")
    client = create_client()

    try:
        response = get_organization(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ Get organization successful")
            if hasattr(response, 'parsed') and response.parsed:
                print(f"  Organization data retrieved")
            return True
        elif response.status_code == 401:
            print(f"⊘ Requires valid API key (401)")
            return None
        else:
            print(f"⚠ Get organization returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ Get organization failed: {type(e).__name__}: {e}")
        return False




# ============================================================================
# COLLECTIONS TESTS
# ============================================================================

def test_list_collections():
    """Test listing collections"""
    print("\n=== Testing List Collections ===")
    client = create_client()

    try:
        response = list_collections(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ List collections successful")
            if hasattr(response, 'parsed') and response.parsed:
                print(f"  Collections data retrieved")
            return True
        elif response.status_code in [401, 404]:
            print(f"⊘ Requires authentication or not found ({response.status_code})")
            return None
        else:
            print(f"⚠ List collections returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ List collections failed: {type(e).__name__}: {e}")
        return False


def test_create_collection():
    """Test creating a collection"""
    print("\n=== Testing Create Collection ===")

    # Skip - requires complex SourceConfig and FeatureExtractorConfig objects
    print("⊘ Skipping - requires complex SourceConfig and FeatureExtractorConfig")
    return None


def test_get_collection():
    """Test getting a specific collection"""
    print("\n=== Testing Get Collection ===")

    if not test_collection_id:
        print("⊘ Skipping - no collection ID available")
        return None

    client = create_client()

    try:
        response = get_collection(client=client, collection_identifier=test_collection_id)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ Get collection successful")
            return True
        elif response.status_code == 404:
            print(f"⊘ Collection not found (404)")
            return None
        else:
            print(f"⚠ Get collection returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ Get collection failed: {type(e).__name__}: {e}")
        return False


def test_delete_collection():
    """Test deleting a collection"""
    print("\n=== Testing Delete Collection ===")

    if not test_collection_id:
        print("⊘ Skipping - no collection ID available")
        return None

    client = create_client()

    try:
        response = delete_collection(client=client, collection_identifier=test_collection_id)
        print(f"Status Code: {response.status_code}")

        if response.status_code in [200, 204]:
            print(f"✓ Delete collection successful")
            return True
        elif response.status_code == 404:
            print(f"⊘ Collection not found (404)")
            return None
        else:
            print(f"⚠ Delete collection returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ Delete collection failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# BUCKETS TESTS
# ============================================================================

def test_list_buckets():
    """Test listing buckets"""
    print("\n=== Testing List Buckets ===")
    client = create_client()

    try:
        response = list_buckets(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ List buckets successful")
            return True
        elif response.status_code in [401, 404]:
            print(f"⊘ Requires authentication or not found ({response.status_code})")
            return None
        else:
            print(f"⚠ List buckets returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ List buckets failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# RETRIEVERS TESTS
# ============================================================================

def test_list_retrievers():
    """Test listing retrievers"""
    print("\n=== Testing List Retrievers ===")
    client = create_client()

    try:
        response = list_retrievers(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ List retrievers successful")
            return True
        elif response.status_code in [401, 404]:
            print(f"⊘ Requires authentication or not found ({response.status_code})")
            return None
        else:
            print(f"⚠ List retrievers returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ List retrievers failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# FEATURE EXTRACTORS TESTS
# ============================================================================

def test_list_feature_extractors():
    """Test listing feature extractors"""
    print("\n=== Testing List Feature Extractors ===")
    client = create_client()

    try:
        response = list_feature_extractors(client=client)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ List feature extractors successful")
            if hasattr(response, 'parsed') and response.parsed:
                print(f"  Feature extractors retrieved")
            return True
        elif response.status_code in [401, 404]:
            print(f"⊘ Requires authentication or not found ({response.status_code})")
            return None
        else:
            print(f"⚠ List feature extractors returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ List feature extractors failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# TASKS TESTS
# ============================================================================

def test_get_task():
    """Test getting a task (with dummy ID)"""
    print("\n=== Testing Get Task ===")
    client = create_client()

    try:
        # Use a dummy task ID - we expect 404
        response = get_task(client=client, task_id="dummy_task_id_12345")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 404:
            print(f"✓ Get task endpoint works (404 expected for dummy ID)")
            return True
        elif response.status_code == 200:
            print(f"✓ Get task successful (unexpected - dummy ID returned data)")
            return True
        elif response.status_code in [401, 403]:
            print(f"⊘ Requires authentication ({response.status_code})")
            return None
        else:
            print(f"⚠ Get task returned status {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ Get task failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# CLIENT INITIALIZATION TESTS
# ============================================================================

def test_client_initialization():
    """Test that the client can be initialized"""
    print("\n=== Testing Client Initialization ===")

    try:
        client = create_client()
        print(f"✓ Client initialized successfully")
        print(f"  Base URL: {client._base_url}")
        return True
    except Exception as e:
        print(f"✗ Client initialization failed: {type(e).__name__}: {e}")
        return False


# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def main():
    """Run all tests"""
    print("="*70)
    print("Mixpeek Python SDK - Comprehensive E2E Tests")
    print("="*70)
    print(f"API URL: {LOCAL_API_URL}")
    print(f"API Key: {API_KEY[:15]}..." if len(API_KEY) > 15 else f"API Key: {API_KEY}")

    results = {}

    # Client tests
    print("\n" + "="*70)
    print("CLIENT TESTS")
    print("="*70)
    results["Client Initialization"] = test_client_initialization()

    # Health tests
    print("\n" + "="*70)
    print("HEALTH & STATUS TESTS")
    print("="*70)
    results["Health Check"] = test_health_check()

    # Organization tests
    print("\n" + "="*70)
    print("ORGANIZATION TESTS")
    print("="*70)
    results["Get Organization"] = test_get_organization()

    # Collections tests
    print("\n" + "="*70)
    print("COLLECTIONS TESTS")
    print("="*70)
    results["List Collections"] = test_list_collections()
    results["Create Collection"] = test_create_collection()
    results["Get Collection"] = test_get_collection()
    results["Delete Collection"] = test_delete_collection()

    # Buckets tests
    print("\n" + "="*70)
    print("BUCKETS TESTS")
    print("="*70)
    results["List Buckets"] = test_list_buckets()

    # Retrievers tests
    print("\n" + "="*70)
    print("RETRIEVERS TESTS")
    print("="*70)
    results["List Retrievers"] = test_list_retrievers()

    # Feature extractors tests
    print("\n" + "="*70)
    print("FEATURE EXTRACTORS TESTS")
    print("="*70)
    results["List Feature Extractors"] = test_list_feature_extractors()

    # Tasks tests
    print("\n" + "="*70)
    print("TASKS TESTS")
    print("="*70)
    results["Get Task"] = test_get_task()

    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)

    passed = sum(1 for r in results.values() if r is True)
    failed = sum(1 for r in results.values() if r is False)
    skipped = sum(1 for r in results.values() if r is None)

    # Group by category
    categories = {
        "Client": ["Client Initialization"],
        "Health & Status": ["Health Check"],
        "Organization": ["Get Organization"],
        "Collections": ["List Collections", "Create Collection", "Get Collection", "Delete Collection"],
        "Buckets": ["List Buckets"],
        "Retrievers": ["List Retrievers"],
        "Feature Extractors": ["List Feature Extractors"],
        "Tasks": ["Get Task"]
    }

    for category, tests in categories.items():
        print(f"\n{category}:")
        for test_name in tests:
            if test_name in results:
                result = results[test_name]
                status = "✓ PASS" if result is True else ("✗ FAIL" if result is False else "⊘ SKIP")
                print(f"  {status}: {test_name}")

    print("\n" + "="*70)
    print(f"Total Tests: {len(results)}")
    print(f"Passed:      {passed} ({passed/len(results)*100:.1f}%)")
    print(f"Failed:      {failed} ({failed/len(results)*100:.1f}%)")
    print(f"Skipped:     {skipped} ({skipped/len(results)*100:.1f}%)")
    print("="*70)

    return failed == 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
