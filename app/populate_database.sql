INSERT INTO users (username, password_hash, email, role, shareable, status)
VALUES
('admin1', 
  '$2b$12$sLDeXJhQn2L/FNv8qGkDL.Cw8BDaszP2/oIPYr2Fmx2kG237Qa3hW',  -- 生成的密码哈希（Admin1pass*）
  'admin1@example.com', 
  'admin', 
  1,
  'active' 
);