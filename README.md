# 최하영 | Infrastructure & Backend Engineer

필요한 기술이 낯설어도 배우고 직접 적용하며, 서버 운영과 소프트웨어 개발을 함께 경험해 왔습니다.
프로그램이 실행되는 환경부터 실제 서비스의 동작까지 이해하는 엔지니어로 성장하고 있습니다.

## 대표 프로젝트

| 프로젝트 | 해결한 문제와 경험 | 자료 |
| --- | --- | --- |
| Kubernetes 모델 세트 전환 연구 | 세트 전환 아키텍처 설계와 순차·병렬 배포 프로토타입 비교. 기존 코드와 결과, 계측의 한계를 함께 공개 | [코드·원본 결과](https://github.com/Headfish96/tsdo-simulation) |
| 퀀트 백테스트 연구 | 리밸런싱 전략, 신호·체결 시점, 비용, 현금흐름을 고려한 Python 기반 전략 비교 연구 | [연구 소개](projects/quant-research.md) |
| Billage | 금융 API 제약을 은행·오픈뱅킹·마이데이터 모의 구현으로 해결한 금전거래 서비스 | [저장소](https://github.com/Headfish96/Billage) |
| PiYou | OnDevice-AI 기반 아동 생활습관 개선 앱. SSAFY 프로젝트 경진대회 전국 1등 | [서버 저장소](https://github.com/Headfish96/PiYou) |
| CodeHive | 실시간 양방향 알고리즘 스터디 웹 플랫폼. SSAFY 공통 프로젝트 우수상 | [저장소](https://github.com/Headfish96/CodeHive) |
| Flightstick Tester | Python 기반 조이스틱 입력 테스트 도구 | [저장소](https://github.com/Headfish96/velocityone-flightstick-tester) |

## Infrastructure & Research

### Kubernetes 모델 세트 전환

여러 모델을 개별적으로 다루는 것을 넘어 상황에 맞는 세트로 전환하는 구조를 연구했습니다.
기존 Python·kubectl 실험과 10회씩의 측정 결과를 아카이브로 정리했습니다.

- **논문:** 전술 임무 단계 이종 AI 모델 세트의 오케스트레이션을 위한 쿠버네티스 커스텀 컨트롤러 설계
- **공동저자:** 최하영, 박범식, 백승호
- **발표:** 한국통신학회 2026년 하계학술대회
- [논문 원문](https://d2j16w31g89z0j.cloudfront.net/site/2026s/abs/0721-ZUPVY.pdf)

공개 코드는 제안 아키텍처 전체의 커스텀 컨트롤러가 아닌 배포 실험 프로토타입입니다.
실제 AI 모델·KEDA·Argo의 통합 성능을 검증한 것으로 표현하지 않으며, 재집계 방법과 구현의 한계는 저장소에 구분해 기록했습니다.

### 서버 구축과 운영

Ubuntu 설치·업데이트와 NVIDIA 드라이버 관리, Kubernetes 클러스터 구성,
Prometheus·Grafana 모니터링, IPMI 원격 관리 환경을 직접 구성했습니다.
물리 서버 유지보수 경험에 소프트웨어 개발 경험을 더해, 서버를 사용하는 개발자의 관점도 함께 이해하고 있습니다.
회사 내부 코드와 비공개 시스템 구성은 공개하지 않습니다.

## Backend & Applied AI

### Billage

**개인 담당:** 기획·발표, 백엔드·인프라. 팀 프로젝트.

차용증 생성부터 송금·상환까지 이어지는 서비스를 개발했습니다.
외부 금융 API 이용 제약에 대응하여 금융 시스템을 모의 구현하고,
MSA와 Spring WebClient·WebFlux 기반 통신을 통해 서비스 간 연결을 다뤘습니다.

### PiYou

**개인 담당:** 기획·발표, 백엔드·AI. 팀 프로젝트.

아이의 식습관과 양치습관 개선을 돕기 위해 MediaPipe와 Unity를 적용했습니다.
Graham Scan 기반 Convex Hull로 손동작 인식을 보완하고,
사용자 상태 갱신에는 정기 실행과 JDBC 배치 처리를 적용했습니다.
링크된 포크는 서버 저장소이며 앱·AI 코드 전체를 포함한다는 뜻은 아닙니다.

## Experience

| 소속 | 경험 |
| --- | --- |
| LIG D&A · C4I연구소 | 제어 SW 개발·유지보수, 서버 환경 구축 및 플랫폼 아키텍처 검토 참여 |
| AWS · Data Center Operations | 물리 서버 장애 상태 확인 및 장비 교체 |
| 멀티캠퍼스 · SSAFY 실습코치 | 2023.12–2024.05, 프리랜서. 교육생 프로젝트 품질 향상 지원·지도 |
| 육군 통신장교 | 서버 운영 관리, 장애 대응 조율 및 저장장치 증설·로그 정책 개선 추진 |

## 기술 경험

- **Infrastructure:** Linux/Ubuntu, Kubernetes, Docker, Prometheus, Grafana, IPMI
- **Development:** Python, Java, Spring, JPA, MySQL, C#, Unity, MediaPipe
- **Systems:** VxWorks 기반 제어 소프트웨어 유지보수·시험평가

기술 목록은 실제 사용 경험을 뜻하며, 모든 항목의 숙련도가 동일하다는 의미는 아닙니다.

[기술 블로그](https://coder-angrybird.tistory.com/) · [알고리즘 학습](https://github.com/Headfish96/Algorithm) · [CS 스터디](https://github.com/Headfish96/CS-Study)

팀 프로젝트의 링크는 포크를 포함합니다. 원본 저장소·공동 작업자의 기여와 개인 담당 역할을 구분합니다.
