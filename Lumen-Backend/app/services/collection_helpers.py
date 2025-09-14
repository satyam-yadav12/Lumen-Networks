from datetime import datetime, timezone
from ..utils.db import increment_counter
def create_collection_data(id, user):
    counter  = increment_counter("likes")
    data   = {
        "like_id": counter,
        "img_id": id,
        "username": user,
        "Liked at": datetime.now(timezone.utc)
    }
    return data                                          


