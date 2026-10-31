import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const guides = defineCollection({
  loader: glob({
    base: './skills',
    pattern: '*/references/guide.ru.md',
    generateId: ({ entry }) => entry.split('/')[0],
  }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    country: z.string(),
    countryCode: z.string().length(2),
    office: z.string(),
    verifiedAt: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    skillName: z.string(),
    scope: z.string(),
  }),
});

export const collections = { guides };
