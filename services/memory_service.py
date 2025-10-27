# --- Import BOTH collections from your existing database file ---
from services.database import remeber_collection, nicknames_collection

# --- General Memory Functions ---

async def save_memory(user_id: str, platform: str, memory_text: str):
    """Saves a piece of text for a user to the 'remeber_collection'."""
    try:
        await remeber_collection.insert_one({
            "user_id": str(user_id),
            "platform": platform,
            "memory": memory_text
        })
        print(f"--- [MEMORY] Saved for {user_id} on {platform}: {memory_text} ---")
    except Exception as e:
        print(f"--- [FAILURE] Could not save memory: {e} ---")

async def get_user_memories(user_id: str, platform: str) -> list[str]:
    """Retrieves all memories for a specific user from the 'remeber_collection'."""
    try:
        cursor = remeber_collection.find({
            "user_id": str(user_id),
            "platform": platform
        })
        memories = [doc["memory"] async for doc in cursor]
        return memories
    except Exception as e:
        print(f"--- [FAILURE] Could not retrieve memories: {e} ---")
        return []

async def set_nickname(user_id: str, platform: str, nickname: str):
    """Sets or updates a nickname for a user."""
    try:
        # This command will find a document that matches the user and platform,
        # and update it. If it doesn't exist, 'upsert=True' will create it.
        await nicknames_collection.update_one(
            {"user_id": str(user_id), "platform": platform},
            {"$set": {"nickname": nickname}},
            upsert=True
        )
        print(f"--- [NICKNAME] Set for {user_id} on {platform}: {nickname} ---")
    except Exception as e:
        print(f"--- [FAILURE] Could not set nickname: {e} ---")

async def get_nickname(user_id: str, platform: str) -> str | None:
    """Gets the nickname for a user, if it exists."""
    try:
        document = await nicknames_collection.find_one({
            "user_id": str(user_id),
            "platform": platform
        })
        if document:
            return document.get("nickname")
        return None
    except Exception as e:
        print(f"--- [FAILURE] Could not get nickname: {e} ---")
        return None