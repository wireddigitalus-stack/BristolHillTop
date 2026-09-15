-- =============================================
-- Bristol Hilltop Camping — Supabase Schema
-- Paste this into Supabase SQL Editor and run
-- =============================================

-- 1. HITS TABLE — every telemetry event
CREATE TABLE IF NOT EXISTS hits (
  id bigserial PRIMARY KEY,
  type text NOT NULL,          -- 'pageview', 'click', 'call', 'text'
  page text,                   -- URL path like '/' or '/blog/'
  device text,                 -- 'Mobile', 'Desktop', 'Tablet'
  source text,                 -- 'Google Search', 'Organic Search', etc.
  label text,                  -- click label like '📞 Phone Call Click'
  created_at timestamptz DEFAULT now()
);

-- 2. LEADS TABLE — form submissions
CREATE TABLE IF NOT EXISTS leads (
  id bigserial PRIMARY KEY,
  name text NOT NULL,
  phone text NOT NULL,
  email text,
  interest text,               -- 'Monthly Rental', 'Yearly Rental', etc.
  message text,
  status text DEFAULT 'new',   -- 'new', 'contacted', 'closed'
  created_at timestamptz DEFAULT now()
);

-- 3. INDEXES for fast dashboard queries
CREATE INDEX IF NOT EXISTS idx_hits_type ON hits(type);
CREATE INDEX IF NOT EXISTS idx_hits_created ON hits(created_at);
CREATE INDEX IF NOT EXISTS idx_leads_status ON leads(status);
CREATE INDEX IF NOT EXISTS idx_leads_created ON leads(created_at);

-- 4. ENABLE ROW LEVEL SECURITY
ALTER TABLE hits ENABLE ROW LEVEL SECURITY;
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;

-- 5. RLS POLICIES — allow anon to insert hits and manage leads
CREATE POLICY "Anyone can insert hits" ON hits
  FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY "Anyone can read hits" ON hits
  FOR SELECT TO anon USING (true);

CREATE POLICY "Anyone can insert leads" ON leads
  FOR INSERT TO anon WITH CHECK (true);

CREATE POLICY "Anyone can read leads" ON leads
  FOR SELECT TO anon USING (true);

CREATE POLICY "Anyone can update leads" ON leads
  FOR UPDATE TO anon USING (true) WITH CHECK (true);
