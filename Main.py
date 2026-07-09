-- Conversations table to track the queue and ownership
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    whatsapp_id VARCHAR(255) UNIQUE NOT NULL, -- The unique ID from Meta
    status VARCHAR(50) DEFAULT 'QUEUED',     -- 'QUEUED', 'CLAIMED', 'CLOSED'
    assigned_agent_id INT,                   -- Null until claimed
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Messages table to track the conversation history
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    conversation_id INT REFERENCES conversations(id),
    sender_type VARCHAR(20),                -- 'CUSTOMER' or 'AGENT'
    message_body TEXT,
    agent_id INT,                           -- Who sent it (if agent)
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
