# Gamma International ERP

Enterprise Resource Planning system for Gamma International — import, manufacturing, and distribution across three branches and four product categories.

## Tech Stack

- **Backend**: FastAPI (Python 3.12) + PostgreSQL + Redis
- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS
- **PDF**: Playwright (headless Chromium)
- **Storage**: MinIO (S3-compatible)
- **Deployment**: Railway (backend) + Vercel (frontend)

## Branches

| Code | Branch |
|------|--------|
| GI | Gamma International (Nasr City) |
| GIE | Gamma International Egypt (Obour City) |
| GEE | Gamma Egypt for Engineering & Trade |

## Categories

LED Lights · Heater & Thermocouple · Solar AC · Trade

## Local Development

```bash
# Start all services
docker-compose up -d

# Backend API
http://localhost:8000/api/docs

# Frontend
http://localhost:3000
```

## Environment Setup

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env.local
# Edit both files with your values
```

## Deployment

- **Backend → Railway**: Connect repo, set root to `backend/`, add env vars
- **Frontend → Vercel**: Connect repo, set root to `frontend/`, add `NEXT_PUBLIC_API_URL`
