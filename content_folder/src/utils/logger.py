# Placeholder for logging utility

import logging
import json
import os

def setup_logger(log_file='logs/agent_logs.json'):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def log_agent_activity(logger, agent_name, activity_type, details):
    log_entry = {
        "agent": agent_name,
        "activity_type": activity_type,
        "details": details
    }
    logger.info(json.dumps(log_entry))

if __name__ == "__main__":
    logger = setup_logger()
    logger.info("Logger initialized.")
    log_agent_activity(logger, "TestAgent", "Start", {"message": "Starting process"})
