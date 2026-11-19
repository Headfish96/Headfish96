"""Build the public developer and teaching portfolios from shared case content."""
from pathlib import Path
from html import escape as e
import json
from portfolio_architecture import ARCH, diagram, case_analysis, gallery, dialog, write_markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
DATA = json.loads((ROOT / 'portfolio-content.json').read_text())
PROJECTS = {p['id']: p for p in DATA['projects']}
BASE = 'https://headfish96.github.io/Headfish96/'

def arrow(prefix=''):
    return ''

def head(title, description, route, prefix='', page=''):
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} · Headfish96</title><meta name="description" content="{e(description)}">
<meta name="theme-color" content="#172d4d"><link rel="canonical" href="{BASE}{route}">
<meta property="og:title" content="{e(title)} · Headfish96"><meta property="og:description" content="{e(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}{route}">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="{prefix}assets/PretendardVariable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{prefix}portfolio.css"><script src="{prefix}portfolio.js" defer></script></head>
<body data-page="{page}"><a class="skip" href="#main">본문으로 이동</a>
<header class="site-header"><div class="wrap header-inner"><a class="brand" href="{prefix}developer.html">Headfish96<span class="brand-dot">.</span></a><nav class="main-nav" aria-label="포트폴리오 선택">
<a href="{prefix}developer.html" {'aria-current="page"' if page == 'developer' else ''}>개발자 포트폴리오</a>
<a href="{prefix}index.html" {'aria-current="page"' if page == 'teaching' else ''}>교육 · 코칭</a>
<a class="external" href="https://github.com/Headfish96">GitHub {arrow(prefix)}</a></nav></div></header>'''

def footer(prefix=''):
    return dialog()+f'''<footer class="site-footer"><div class="wrap footer-inner"><p>Headfish96 · Software Engineer<br>시스템 개발, 서비스 구현, 그리고 함께 배우는 과정.</p><p><a href="{prefix}developer.html">개발자 포트폴리오</a> &nbsp; / &nbsp; <a href="{prefix}index.html">교육 · 코칭</a><br>Updated 2026.11</p></div></footer></body></html>'''

def tags(values):
    return '<ul class="tags" aria-label="사용 기술">'+''.join(f'<li>{e(x)}</li>' for x in values)+'</ul>'

def section_head(num, title, desc=''):
    return f'<div class="section-head"><div><p class="eyebrow">{num}</p><h2>{title}</h2></div>'+ (f'<p>{desc}</p>' if desc else '')+'</div>'

SHORT = {'rtos':'RTOS / VxWorks','serial-simulator':'RS232 통신 모의 프로그램','mds':'MDS','model-transition':'Kubernetes 모델 세트 전환 연구'}
def project_row(id, n):
    p=PROJECTS[id]
    label={'rtos':'실무 개발 · 시험평가','serial-simulator':'저작권 등록','mds':'AI 협업 · 개발 중','model-transition':'학술대회 발표'}[id]
    return f'''<article class="project-item" id="{id}"><span class="project-num">{n:02}</span><div><h3><a href="projects/{id}.html">{e(SHORT[id])} {arrow()}</a></h3><p class="summary">{e(p['subtitle'])}</p></div><div class="project-meta"><strong>{e(p['role'])}</strong><span class="status">{label}</span>{tags(p['tags'][:4])}</div></article>'''

def showcase(id):
    p=PROJECTS[id]
    image=p['image']
    if id=='billage':
        media=''.join(f'<img src="assets/billage-{name}.webp" alt="Billage {alt}" loading="lazy" width="270" height="550">' for name,alt in [('home','거래 현황 화면'),('contract','차용증 화면'),('history','거래 내역 화면')])
    else:
        media=f'<img src="{e(image["src"])}" alt="{e(image["alt"])}" loading="lazy">'
    recognition='SSAFY 전국 1등 · 팀 수상' if id=='piyou' else '팀 프로젝트'
    return f'''<article class="showcase-card" id="{id}"><a class="showcase-media {id}" href="projects/{id}.html" aria-label="{p['title']} 상세 사례">{media}</a><div class="showcase-copy"><div class="kicker"><span>{e(p['category'])}</span><span>{recognition}</span></div><h3><a href="projects/{id}.html">{p['title']} {arrow()}</a></h3><p>{e(p['subtitle'])}</p><p class="role">{e(p['role'])}</p></div></article>'''

def experience():
    rows=[('2025 — 현재','LIG Defense & Aerospace','C4I연구소','VxWorks 기반 미사일 체계 소프트웨어 개발·유지보수·시험평가, 서버 환경 구축 및 플랫폼 아키텍처 검토 참여.'),('2024.07 입사','AWS','Data Center Operations','물리 서버 장애 상태 확인 및 장비 교체.'),('2023.12 — 2024.05','멀티캠퍼스','SSAFY 프로젝트 실습코치','교육생 프로젝트 품질 향상 지원·지도.'),('2020 — 2022','대한민국 육군','정보통신장교','서버 운영, 장애 대응 조율과 저장장치 증설 경험.')]
    return '<div class="experience-list">'+''.join(f'<article class="experience-item"><time>{date}</time><div><h3>{name}</h3><p class="role">{role}</p><p>{text}</p></div></article>' for date,name,role,text in rows)+'</div>'

CATEGORY={'rtos':'systems','serial-simulator':'systems','mds':'tools','piyou':'services','billage':'services','codehive':'services','argus':'tools','flightstick':'systems','maknae':'tools','model-transition':'research'}
def archive():
    filters=[('all','전체'),('systems','시스템 · 연동'),('services','서비스'),('tools','개발 도구'),('research','연구')]
    result='<div class="archive-top"><div class="filters" role="group" aria-label="프로젝트 분야">'+''.join(f'<button class="filter" type="button" data-filter="{v}" aria-pressed="{str(v=="all").lower()}">{text}</button>' for v,text in filters)+'</div><p class="result-count" aria-live="polite" data-result-count>10개 프로젝트</p></div><div class="archive-grid">'
    for p in DATA['projects']:
        result+=f'''<article class="archive-item" data-project-category="{CATEGORY[p['id']]}"><p class="category">{e(p['category'])}</p><h3><a href="projects/{p['id']}.html">{e(SHORT.get(p['id'],p['title']))} {arrow()}</a></h3><p>{e(p['subtitle'])}</p><a class="details-link" href="projects/{p['id']}.html">역할과 구현 내용 보기</a></article>'''
    return result+'</div>'

developer=head('개발자 포트폴리오','VxWorks RTOS, 통신 모의 프로그램, 백엔드와 인프라. Headfish96의 개발·설계 사례와 공개 프로젝트.','developer.html',page='developer')
developer+='''<main id="main"><div class="wrap"><section class="engineering-hero" aria-labelledby="intro-heading"><div><p class="hero-identity">HEADFISH96 / SOFTWARE ENGINEER</p><h1 id="intro-heading">실시간 시스템부터<br><span>연결되는 서비스까지.</span></h1><p class="hero-subline">VxWorks 기반 체계 소프트웨어, 장비 연동 도구, 백엔드 서비스를 개발합니다. 코드의 동작과 설계 선택을 프로젝트별로 정리했습니다.</p><div class="hero-links"><a class="button" href="#selected">프로젝트 살펴보기</a><a class="text-link" href="https://github.com/Headfish96">GitHub</a><a class="text-link" href="https://coder-angrybird.tistory.com/">기술 블로그</a></div><div class="hero-tokens"><span>RTOS · VxWorks</span><span>Python · Java</span><span>Backend · Integration</span></div></div><a class="hero-diagram-link" href="projects/piyou.html#architecture"><img src="assets/architecture/piyou.svg" alt="PiYou의 API·예약 작업·데이터 저장·알림 연결 구조"><div><p class="eyebrow">Inside the project / PiYou</p><strong>기능을 만든 코드, 그 안의 구조.</strong><p>상태 갱신과 알림 발송이 어떻게 연결되는지 살펴보세요.</p></div></a></section><div class="credibility-strip"><div><strong>LIG Defense & Aerospace</strong><p>C4I연구소 · 2025–현재</p></div><div><strong>RS232 통신 모의 프로그램</strong><p>화면·구조 설계 및 구현 · 저작권 등록</p></div><div><strong>SSAFY 전국 1등</strong><p>PiYou · 자율 프로젝트 팀 수상</p></div></div>
<nav class="section-nav" aria-label="페이지 목차"><a href="#selected"><span class="number">01</span>대표 작업</a><a href="#engineering"><span class="number">02</span>코드와 구조</a><a href="#experience"><span class="number">03</span>경력</a><a href="#archive"><span class="number">04</span>전체 프로젝트</a><a href="#skills"><span class="number">05</span>기술 · 기록</a><span class="meta">SYSTEMS / SERVICES / TOOLS</span></nav>
<section class="section" id="selected">'''+section_head('01 / Selected work','직접 개발하고, 설계한 작업','실무 시스템과 연동 도구, 팀 서비스에서<br>맡은 역할과 구현 내용을 소개합니다.')+'<div class="project-list">'+''.join(project_row(id,i+1) for i,id in enumerate(['rtos','serial-simulator','mds']))+'</div><div class="showcase">'+showcase('piyou')+showcase('billage')+'''</div><a class="inline-more" href="projects/model-transition.html"><div><p>Kubernetes 모델 세트 전환 연구</p><span>한국통신학회 2026년 하계학술대회 · 공동 연구 · 공개 실험 아카이브</span></div><span>연구 사례 보기 '''+arrow()+'''</span></a></section>
<section class="section" id="experience">'''+section_head('03 / Experience','개발과 운영을 거쳐온 경력')+experience()+'''</section>
<section class="section" id="archive">'''+section_head('04 / Project archive','전체 프로젝트','분야를 선택해 관련 경험을 모아 볼 수 있습니다.')+archive()+'''</section>
<section class="section" id="skills">'''+section_head('05 / Skills & notes','프로젝트에서 사용한 기술')+'''<div class="skill-grid"><article class="skill-block"><h3>시스템 · 데스크톱</h3><p>VxWorks · RTOS<br>Python · PyQt · pyserial · SQLite<br>MVVM · Repository / DAO</p></article><article class="skill-block"><h3>백엔드 · 인프라</h3><p>Java · Spring Boot · JPA · MySQL<br>WebClient · Linux · Docker · Kubernetes<br>Prometheus · Grafana · IPMI</p></article><article class="skill-block"><h3>AI 적용 · 개발 도구</h3><p>MediaPipe · Unity · pandas · NumPy<br>ChatGPT · Codex · Claude Code<br>EXAONE · vLLM 설치·연동 경험</p></article></div><details class="learning"><summary>학습 기록과 공개 자료</summary><div class="learning-links"><a href="https://github.com/Headfish96/Algorithm">알고리즘</a><a href="https://github.com/Headfish96/CS-Study">CS 스터디</a><a href="https://github.com/Headfish96/Today-I-Learn">TIL</a><a href="https://github.com/Headfish96/Online-Judge">온라인 저지</a><a href="https://github.com/Headfish96/PY4E_Boostcourse">Python 실습</a><a href="https://github.com/Headfish96/Headfish96/blob/main/projects/quant-research.md">데이터 분석 연구</a></div></details></section>
<section class="contact-strip"><div><h2>만든 것에서 더 자세히.</h2><p>코드와 개발 기록, 교육·코칭 경험을 이어서 볼 수 있습니다.</p></div><div class="contact-links"><a class="text-link" href="https://github.com/Headfish96">GitHub '''+arrow()+'''</a><a class="text-link" href="index.html">교육 · 코칭 '''+arrow()+'''</a></div></section></div></main>'''+footer()
developer=developer.replace('<section class="section" id="experience">', '<section class="section" id="engineering">'+section_head('02 / Engineering case studies','어떻게 연결되고, 왜 나눴는가','구조도와 주요 동작 흐름에서<br>설계 선택과 실제 코드로 이어집니다.')+gallery(PROJECTS)+'</section><section class="section" id="experience">')
(DOCS/'developer.html').write_text(developer)

teaching=head('교육·코칭 포트폴리오','SSAFY 프로젝트 실습코치 경험과 AI 협업 개발을 바탕으로 교육생의 실습을 돕는 개발자 Headfish96.','',page='teaching')
teaching+='''<main id="main"><div class="wrap"><section class="hero coach-hero" aria-labelledby="intro-heading"><div><p class="eyebrow">Developer & Project Coach</p><h1 id="intro-heading">개발하는 경험을,<br><span>함께 배우는 힘으로.</span></h1><p class="lead">SSAFY 프로젝트 실습코치로 교육생의 개발 과정을 지원했습니다. 지금도 소프트웨어를 만들며, ChatGPT·Codex를 구현과 검토 과정에 활용합니다.</p><div class="hero-links"><a class="button" href="#coaching">교육 경험 보기'''+arrow()+'''</a><a class="text-link" href="#availability">활동 가능 일정</a></div></div><aside class="coach-proof"><p class="eyebrow">Teaching experience</p><h2>SSAFY<br>프로젝트 실습코치</h2><p class="period">멀티캠퍼스 · 2023.12 — 2024.05</p><p>SSAFY 수료 후 실습코치로 참여해<br>교육생 프로젝트의 품질 향상을 지원·지도했습니다.</p><a class="note-link" href="developer.html#experience">전체 개발 경력 보기 '''+arrow()+'''</a></aside></section>
<nav class="section-nav" aria-label="페이지 목차"><a href="#coaching"><span class="number">01</span>교육 경험</a><a href="#practice"><span class="number">02</span>실습 지원</a><a href="#projects"><span class="number">03</span>개발 사례</a><a href="#availability"><span class="number">04</span>활동 일정</a><span class="meta">DEVELOPMENT × COACHING</span></nav>
<section class="section coach-layout" id="coaching">'''+section_head('01 / Coaching','프로젝트를 만든 뒤,<br>교육생 곁에서.')+'''<div class="coach-body"><p>팀장으로 기획·개발·발표를 맡았던 경험을 바탕으로 실습코치 활동을 이어갔습니다. 백엔드, 서비스 연동, 개발 환경을 직접 다뤄온 경험을 교육생의 프로젝트 지원에 연결합니다.</p><div class="focus-grid"><article class="focus-item"><span class="label">PROJECT</span><h3>개발 과정 이해</h3><p>요구사항을 기능으로 나누고, API·데이터·화면이 연결되는 흐름을 함께 살펴봅니다.</p></article><article class="focus-item"><span class="label">DEBUGGING</span><h3>오류 확인과 설명</h3><p>입력, 실행 환경, 로그를 확인하며 문제를 좁히는 접근을 실습에 적용합니다.</p></article><article class="focus-item"><span class="label">AI CODING</span><h3>AI와 구현·검토</h3><p>MDS 개발에서 요구를 설명하고 AI의 구현을 실행·확인하며 다음 수정으로 이어갑니다.</p></article></div></div></section>
<section class="section coach-layout" id="practice">'''+section_head('02 / In the classroom','실습을 돕는 순서')+'''<div><p class="note" style="margin-bottom:20px">보조강사 활동에서 적용할 지원 방식입니다.</p><ol class="practice-list"><li><div><h3>같은 화면에서 시작합니다.</h3><p>하려던 작업, 입력한 내용, 오류 메시지를 함께 확인합니다. 현재 상태를 먼저 이해하고 다음 확인 항목을 정합니다.</p></div></li><li><div><h3>한 번에 하나씩 확인합니다.</h3><p>실행 환경·입력·API 응답 등 확인할 지점을 나누어 봅니다. 어디서 기대와 달라졌는지 작은 단위로 좁힙니다.</p></div></li><li><div><h3>직접 실행하며 마무리합니다.</h3><p>수정한 이유를 설명하고 수강생이 다시 실행하도록 돕습니다. 같은 문제가 생겼을 때 확인할 순서도 함께 정리합니다.</p></div></li></ol></div></section>
<section class="section" id="projects">'''+section_head('03 / Built & explained','설명의 바탕이 되는 개발 경험','직접 만든 결과물과 설계·발표 경험을<br>프로젝트 사례로 소개합니다.')+'''<div class="coach-projects">'''+showcase('piyou')+'''<article class="mini-case"><span class="eyebrow">AI-assisted development</span><h3>MDS</h3><p>여러 데이터를 시나리오로 편집하고 송신하는 도구를 ChatGPT·Codex와 협업해 개발하고 있습니다. 요구 설명부터 구현 결과 확인·수정까지의 과정을 경험하고 있습니다.</p><a class="text-link" href="projects/mds.html">AI 협업 개발 과정 '''+arrow()+'''</a></article><article class="mini-case"><span class="eyebrow">Design & communication</span><h3>RS232 통신 모의 프로그램</h3><p>UI·소프트웨어 구조·통신·데이터 처리를 설계하고 구현했습니다. 다이어그램과 발표 자료로 설계 선택을 설명했으며, 프로그램은 저작권 등록됐습니다.</p><a class="text-link" href="projects/serial-simulator.html">설계와 구현 내용 '''+arrow()+'''</a></article></div>
<a class="inline-more" href="projects/codehive.html"><div><p>CodeHive · 함께 공부하는 플랫폼</p><span>기획·발표·백엔드 담당 · SSAFY 공통 프로젝트 우수상</span></div><span>프로젝트 보기 '''+arrow()+'''</span></a>
<div class="focus-grid" id="ai"><article class="focus-item"><span class="label">현재 개발에 활용</span><h3>ChatGPT · Codex</h3><p>요구사항 정리, 구현 결과 검토, 오류 재현과 수정에 활용합니다.</p></article><article class="focus-item"><span class="label">사용 경험</span><h3>Claude Code</h3><p>코딩 도구로 직접 사용하며 기본 작업 흐름을 경험했습니다.</p></article><article class="focus-item"><span class="label">설치·적용 경험</span><h3>로컬 GPU · EXAONE</h3><p>Codex와 함께 로컬 GPU에 모델과 문서 검색 하네스를 설치·적용했습니다.</p></article></div>
<p class="note" style="margin-top:25px">도구별 실제 사용 경험을 바탕으로 과정과 지원 범위를 협의합니다.</p></section>
<section class="section" id="availability"><div class="schedule"><div><p class="eyebrow">04 / Availability</p><h2 style="margin-top:12px">가능한 일정에,<br>집중해서 참여합니다.</h2><p>현재 재직 중으로 교육 일정과 참여 가능 시간을 사전에 협의합니다.</p></div><ul><li><strong>주말</strong><span>우선 참여 희망</span></li><li><strong>평일 저녁</strong><span>늦은 시간 참여 가능</span></li><li><strong>짧은 평일 교육</strong><span>일정 협의 시 휴가를 사용해 참여 가능</span></li></ul></div></section>
<section class="contact-strip"><div><h2>개발 경험도 함께 살펴보세요.</h2><p>RTOS·장비 연동·백엔드·인프라까지, 전체 작업을 정리했습니다.</p></div><div class="contact-links"><a class="button" href="developer.html">개발자 포트폴리오 '''+arrow()+'''</a><a class="text-link" href="https://github.com/Headfish96">GitHub</a></div></section></div></main>'''+footer()
teaching=teaching.replace('<div class="focus-grid" id="ai">','<section class="teaching-architecture"><div class="section-head"><div><p class="eyebrow">Explain with a diagram</p><h2>코드의 흐름을 그림으로 설명합니다.</h2></div><p>데이터가 이동하는 순서를 짚고<br>실제 구현과 연결해 살펴볼 수 있는 사례입니다.</p></div>'+gallery(PROJECTS,('codehive','maknae'))+'</section><div class="focus-grid" id="ai">')
(DOCS/'index.html').write_text(teaching)

(DOCS/'projects').mkdir(exist_ok=True)
for i,p in enumerate(DATA['projects']):
    id=p['id']; prefix='../'
    page=head(p['title'],p['subtitle'],f'projects/{id}.html',prefix,page='case')
    page+=f'''<main id="main"><div class="wrap"><nav class="bread" aria-label="현재 위치"><a href="../developer.html">개발자 포트폴리오</a><span aria-hidden="true">/</span><span>{e(SHORT.get(id,p['title']))}</span></nav><header class="case-hero"><p class="eyebrow">{e(p['category'])}</p><h1>{e(p['title'])}</h1><p class="lead">{e(p['summary'])}</p>{tags(p['tags'])}</header><dl class="case-meta"><div><dt>역할</dt><dd>{e(p['role'])}</dd></div><div><dt>상태</dt><dd>{e(p['status'])}</dd></div><div><dt>핵심 작업</dt><dd>{e(p['subtitle'])}</dd></div></dl>'''
    if id in ARCH:
        page+='<nav class="case-nav" aria-label="프로젝트 목차"><a href="#architecture">구조도</a><a href="#flow">동작 흐름</a>' + ('<a href="#decisions">설계 선택과 코드</a>' if ARCH[id].get('decisions') else '') + '<a href="#review">확인 범위</a></nav>'
        page+=diagram(id,prefix)
    if p.get('image'):
        image=p['image']
        if id=='billage':
            srcs=''.join(f'<img src="../assets/billage-{name}.webp" alt="Billage {alt}" loading="lazy">' for name,alt in [('home','거래 현황'),('contract','차용증'),('history','거래 내역')])
            page+=f'<figure class="case-figure"><div class="image-gallery">{srcs}</div><figcaption>Billage 팀 프로젝트의 실제 앱 화면</figcaption></figure>'
        else:
            page+=f'<figure class="case-figure"><img src="../{e(image["src"])}" alt="{e(image["alt"])}"><figcaption>{e(image["caption"])}</figcaption></figure>'
    page+='<div class="case-content"><div>'
    for s in p['sections']:
        page+=f'<section class="case-section"><h2>{e(s["title"])}</h2><p>{e(s["body"])}</p></section>'
    page+=case_analysis(id)
    page+='</div><aside class="case-aside"><div class="case-outcome"><h2>'+('수행 업무' if id=='rtos' else '결과와 산출물')+f'</h2><p>{e(p["outcome"])}</p></div>'
    external=[l for l in p['links'] if not l['url'].startswith(BASE)]
    if external:
        page+='<p class="aside-label">RELATED LINKS</p><div class="case-links">'+''.join(f'<a href="{e(l["url"])}">{e(l["label"])} {arrow(prefix)}</a>' for l in external)+'</div>'
    page+=f'<p class="scope">{e(p["scope"])}</p></aside></div>'
    nextp=DATA['projects'][(i+1)%len(DATA['projects'])]
    page+=f'<nav class="case-next" aria-label="다른 프로젝트"><div><p>NEXT PROJECT</p><a href="{nextp["id"]}.html">{e(SHORT.get(nextp["id"],nextp["title"]))} {arrow(prefix)}</a></div><a class="text-link" href="../developer.html#archive">전체 프로젝트 목록</a></nav></div></main>'+footer(prefix)
    (DOCS/'projects'/f'{id}.html').write_text(page)
print(f'Built teaching, developer and {len(PROJECTS)} case pages.')

write_markdown(PROJECTS)
