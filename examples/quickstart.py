"""
Mixpeek Python SDK - Quick Start Example

This example demonstrates basic usage of the Mixpeek SDK.
Before running, set your API key as an environment variable:

    export MIXPEEK_API_KEY="your_api_key_here"
"""

from mixpeek import Mixpeek, ApiException


def main():
    # Initialize the client (reads MIXPEEK_API_KEY from environment)
    # Or pass api_key directly: Mixpeek(api_key="your_key")
    try:
        client = Mixpeek()
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set your MIXPEEK_API_KEY environment variable:")
        print("  export MIXPEEK_API_KEY='your_key_here'")
        return

    print("Mixpeek SDK Quick Start\n")

    # 1. List collections
    print("Working with Collections...")
    try:
        result = client.collections.list()
        print(f"  Found {len(result.collections)} collection(s)")
        for collection in result.collections[:3]:
            print(f"    - {collection.alias}: {collection.collection_id}")
    except ApiException as e:
        print(f"  Error: {e.reason}")
        if e.status == 401:
            print("    Check your API key!")
        return

    # 2. Create a collection
    print("\nCreating a new collection...")
    collection_alias = "quickstart_demo"

    try:
        collection = client.collections.create(
            alias=collection_alias,
            description="Demo collection from quickstart",
        )
        print(f"  Created collection: {collection.collection_id}")
    except ApiException as e:
        if e.status == 409:
            print(f"  Collection '{collection_alias}' already exists")
            collection = client.collections.get(collection_alias)
        else:
            print(f"  Error: {e.reason}")
            return

    # 3. Add documents
    print("\nAdding documents...")
    sample_docs = [
        {
            "document_id": "doc_1",
            "metadata": {
                "title": "Getting Started with Mixpeek",
                "content": "Mixpeek is a powerful multimodal search platform",
                "category": "tutorial"
            }
        },
        {
            "document_id": "doc_2",
            "metadata": {
                "title": "Advanced Features",
                "content": "Learn about clustering and taxonomy features",
                "category": "guide"
            }
        }
    ]

    for doc_data in sample_docs:
        try:
            result = client.documents.create(
                collection=collection_alias,
                document_id=doc_data["document_id"],
                metadata=doc_data["metadata"]
            )
            print(f"  Added: {result.document_id}")
        except ApiException as e:
            print(f"  Error adding {doc_data['document_id']}: {e.reason}")

    # 4. List documents
    print("\nListing documents...")
    try:
        result = client.documents.list(collection_alias)
        print(f"  Found {len(result.documents)} document(s)")
        for doc in result.documents:
            title = doc.metadata.get('title', 'Untitled')
            print(f"    - {doc.document_id}: {title}")
    except ApiException as e:
        print(f"  Error: {e.reason}")

    # 5. Check retrievers
    print("\nChecking retrievers...")
    try:
        result = client.retrievers.list()
        if result.retrievers:
            print(f"  Found {len(result.retrievers)} retriever(s)")
            for retriever in result.retrievers[:3]:
                print(f"    - {retriever.alias}")
        else:
            print("  No retrievers configured yet")
    except ApiException as e:
        print(f"  Retrievers not available: {e.reason}")

    print("\nQuick start complete!")
    print("\nNext steps:")
    print("  - Explore more examples in the examples/ directory")
    print("  - Read the docs at https://docs.mixpeek.com")


if __name__ == "__main__":
    main()
