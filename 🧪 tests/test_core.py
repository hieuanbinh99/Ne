import pytest
from src.ne_agent.core.processor import Processor

def test_processor_initialization():
    config = {"name": "test-model", "temperature": 0.7}
    processor = Processor(config)
    assert processor.config == config

def test_generate_response():
    config = {"name": "test-model", "temperature": 0.7}
    processor = Processor(config)
    result = processor.generate_response("test input")
    assert "Processed: test input" in result
