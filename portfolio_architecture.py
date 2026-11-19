"""Shared architecture figures and code-reading sections for the portfolio."""
from html import escape as e
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / 'architecture-content.json'
ARCH = {p['id']: p for p in json.loads(CONTENT.read_text())['projects']} if CONTENT.exists() else {}

def diagram(id, prefix='', compact=False):
    a = ARCH.get(id)
    if not a:
        return ''
    src = f'{prefix}assets/architecture/{id}.svg'
    if compact:
        return f'<img src="{src}" alt="{e(a["alt"])}" loading="lazy">'
    links = f'<a href="{src}" target="_blank" rel="noopener">SVG 원본</a><a href="{prefix}assets/architecture/{id}.mmd" download>Mermaid 소스</a>'
    if a.get('figjam'):
        links += f'<a href="{e(a["figjam"])}" target="_blank" rel="noopener">FigJam에서 편집</a>'
    return f'''<section class="architecture-section" id="architecture" aria-labelledby="architecture-title">
      <div class="architecture-heading"><div><p class="eyebrow">Architecture / Flow</p><h2 id="architecture-title">{e(a['diagramTitle'])}</h2></div>
      <div class="diagram-toolbar"><button type="button" data-diagram="{src}" data-diagram-title="{e(a['diagramTitle'])}">확대해서 보기</button>{links}</div></div>
      <figure><div class="diagram-surface"><img src="{src}" alt="{e(a['alt'])}" loading="eager"></div>
      <figcaption class="architecture-caption">{e(a['caption'])}</figcaption></figure></section>'''

def case_analysis(id):
    a = ARCH.get(id)
    if not a:
        return ''
    result = '<div class="technical-analysis">'
    if a.get('flow'):
        result += '<section class="case-section" id="flow"><p class="eyebrow">Follow the data</p><h2>동작 흐름을 따라가면</h2><ol class="flow-list">'
        for step in a['flow']:
            if isinstance(step, str):
                result += f'<li>{e(step)}</li>'
            else:
                result += f'<li><h3>{e(step["title"])}</h3><p>{e(step["description"])}</p></li>'
        result += '</ol></section>'
    if a.get('decisions'):
        result += '<section class="case-section" id="decisions"><p class="eyebrow">Engineering decisions</p><h2>구현에서 읽을 수 있는 설계 선택</h2><div class="decision-list">'
        for d in a['decisions']:
            result += f'<article class="decision-item"><h3>{e(d["title"])}</h3><p>{e(d["description"])}</p>'
            if d.get('tradeoff'):
                result += f'<p class="tradeoff"><strong>고려할 점</strong> {e(d["tradeoff"])}</p>'
            if d.get('evidence'):
                result += '<ul class="source-list">'
                for s in d['evidence'][:2]:
                    label=s.get('label') or s['path'].split('/')[-1]
                    result += f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener"><code>{e(label)}</code><span>근거 코드</span></a></li>'
                result += '</ul>'
            result += '</article>'
        result += '</div></section>'
    if a.get('limitations'):
        result += '<section class="case-section" id="review"><h2>확인 범위와 남은 과제</h2><ul class="review-note">'+''.join(f'<li>{e(s)}</li>' for s in a['limitations'])+'</ul>'
        if a.get('commit'):
            result += f'<p class="source-version">코드 기준 <a href="{e(a["repo"])}/tree/{e(a["commit"])}"><code>{e(a["commit"][:7])}</code></a> · 구조와 주요 실행 경로를 정적으로 검토했습니다.</p>'
        result += '</section>'
    return result+'</div>'

def card(id, projects):
    p=projects[id]; a=ARCH[id]
    return f'''<article class="architecture-card"><a class="architecture-preview" href="projects/{id}.html#architecture" aria-label="{e(p['title'])} 구조도 보기">{diagram(id,compact=True)}</a><div class="architecture-card-copy"><p class="eyebrow">{e(p['category'])}</p><h3><a href="projects/{id}.html">{e(p['title'])}</a></h3><p>{e(a['teaser'])}</p><p class="role">{e(p['role'])}</p><a class="text-link" href="projects/{id}.html#architecture">구조와 설계 선택 살펴보기</a></div></article>'''

def gallery(projects, ids=('piyou','codehive','billage','argus')):
    return '<div class="architecture-gallery">'+''.join(card(id,projects) for id in ids if id in ARCH)+'</div>'

def dialog():
    return '''<dialog class="diagram-dialog" aria-labelledby="diagram-dialog-title"><div class="dialog-header"><h2 class="dialog-title" id="diagram-dialog-title">아키텍처 확대</h2><button class="close" type="button" data-close-diagram aria-label="구조도 확대 닫기">닫기</button></div><p class="dialog-help">넓은 그림은 좌우로 스크롤해 확인할 수 있습니다.</p><div class="dialog-canvas"><img alt=""></div></dialog>'''

def write_markdown(projects):
    dest=ROOT/'projects/architecture'
    dest.mkdir(parents=True,exist_ok=True)
    for id,a in ARCH.items():
        p=projects[id]
        lines=[f'# {p["title"]} · 구조와 구현', '', f'**담당 역할:** {p["role"]}', '',
               f'[웹 포트폴리오](https://headfish96.github.io/Headfish96/projects/{id}.html)', '',
               f'## {a["diagramTitle"]}', '', a['caption'], '',
               f'![{a["alt"]}](../../docs/assets/architecture/{id}.svg)', '',
               '<details>', '<summary>Mermaid 원본</summary>', '', '```mermaid', a['mermaid'], '```', '', '</details>', '',
               '## 동작 흐름', '']
        for i,step in enumerate(a['flow'],1):
            lines += [f'{i}. **{step["title"]}** — {step["description"]}']
        if a.get('decisions'):
            lines += ['', '## 구현에서 읽을 수 있는 설계 선택', '']
            for d in a['decisions']:
                lines += [f'### {d["title"]}', '', d['description'], '']
                if d.get('tradeoff'):
                    lines += [f'고려할 점: {d["tradeoff"]}', '']
                for ev in d.get('evidence',[]):
                    lines += [f'- [{ev["path"]} · {ev["lines"]}]({ev["url"]})']
                lines += ['']
        lines += ['## 확인 범위', '']+['- '+s for s in a['limitations']]
        if a.get('commit'):
            lines += ['',f'코드 기준: [{a["commit"][:7]}]({a["repo"]}/tree/{a["commit"]}). 구조와 주요 실행 경로를 정적으로 검토했습니다.']
        if a.get('figjam'):
            lines += ['',f'[FigJam 편집 원본]({a["figjam"]})']
        (dest/(id+'.md')).write_text('\n'.join(lines)+'\n')
