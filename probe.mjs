
import { getCollection } from 'astro:content';
const products = await getCollection('products');
console.log('products 数:', products.length);
if (products.length > 0) {
  const p = products[0];
  console.log('keys:', Object.keys(p).join(','));
  console.log('id:', p.id);
  console.log('slug:', p.slug);
  console.log('data.title:', p.data.title);
}
const guides = await getCollection('guides');
console.log('guides 数:', guides.length);
if (guides.length > 0) {
  const g = guides[0];
  console.log('guides keys:', Object.keys(g).join(','));
  console.log('guide id:', g.id, '| slug:', g.slug);
}
