// CamlockPro 作者档案（作者 = 本人 Ray Chan / 陈琪瑞, 与 brickswiki/chanzipu 同源人设）
// 用于文章详情页/卡片的 byline 与 /author/ 单页：头像+名字+阅读时间
export interface Author {
  id: string;
  name: string;
  role: string;
  bio: string;
  initials: string;
  avatarBg: string;
  avatarImg?: string;
}

export const DEFAULT_AUTHOR: Author = {
  id: 'raychan',
  name: 'Ray Chan',
  role: 'Hose application engineer · CamlockPro',
  bio: 'Industrial hose specialist. I spec food grade, PTFE, chemical, hydraulic and silicone hoses against real duty conditions — fluid, pressure, temperature and cleaning regime — rather than catalogue numbers. Every guide here comes from actual specification work.',
  initials: 'RC',
  avatarBg: 'var(--c-brand)',
  avatarImg: '/images/authors/ray-chan.jpg',
};

// 阅读时间：按英文 200 词/分钟估算
export function readingTime(body: string): number {
  if (!body) return 1;
  const words = body.trim().split(/\s+/).length;
  return Math.max(1, Math.ceil(words / 200));
}
