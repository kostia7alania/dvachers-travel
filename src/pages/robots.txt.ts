import type { APIRoute } from 'astro';

export const GET: APIRoute = ({ site }) => {
  if (!site) throw new Error('Set site in astro.config.mjs.');
  const base = new URL(import.meta.env.BASE_URL, site);
  return new Response(`User-agent: *\nAllow: /\nSitemap: ${new URL('sitemap.xml', base).href}\n`, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
