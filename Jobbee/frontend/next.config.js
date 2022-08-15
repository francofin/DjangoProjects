/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  env:{
    API_URL:'http://localhost:8000',
    MAPBOX_ACCESS_TOKEN:'pk.eyJ1IjoiZnJhbmNvZmluIiwiYSI6ImNsNm9nNmIzYzBhbnIzaXRlNTJranJwankifQ.8EBtyLcfgqaQYIWn3y1pbA'
  }
}

module.exports = nextConfig
