
from pydantic import BaseModel, ConfigDict


class TopicClusterBase(BaseModel):
    label: str
    keywords: str

class TopicClusterCreate(TopicClusterBase):
    pass

class TopicClusterInDBBase(TopicClusterBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class TopicCluster(TopicClusterInDBBase):
    pass
