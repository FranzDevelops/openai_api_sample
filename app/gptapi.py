import os
import openai
from .config import settings
openai.organization = "org-LkkVXsGWzO96L2wIvMPjYoOw"
openai.api_key = settings.openai_api_key
openai.Model.list()