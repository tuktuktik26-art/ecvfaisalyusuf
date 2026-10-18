import io
from xml.sax.saxutils import escape

import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.units import cm

# ============================================================
# E-CV Faisal Yusuf | Mata Kuliah Digital Kreatif
# Perbarui data di bagian PROFILE. Jangan menambahkan informasi
# yang belum benar atau belum dapat diverifikasi.
# ============================================================
PROFILE = {
    "name": "Faisal Yusuf",
    "headline": "Mahasiswa S1 Sistem Informasi",
    "campus": "Universitas Bina Sarana Informatika",
    "semester": "Semester 5",
    "email": "fslysf2334@gmail.com",
    "about": (
        "Saya adalah mahasiswa S1 Sistem Informasi di Universitas Bina Sarana "
        "Informatika. Saya tertarik mengembangkan pengetahuan dan keterampilan "
        "digital melalui pembelajaran serta proyek perkuliahan. Saya juga memiliki "
        "pengalaman PKL di bidang Komunikasi dan Informasi Publik pada bagian siaran radio."
    ),
    "education": [
        {"institution": "Universitas Bina Sarana Informatika", "program": "S1 Sistem Informasi", "period": "Semester 5"},
        {"institution": "SMA Negeri 1 Samigaluh", "program": "Pendidikan menengah", "period": "[Tambahkan tahun jika diperlukan]"},
    ],
    "technical_skills": ["Canva"],
    "soft_skills": ["Komunikasi", "Kerja sama tim"],
    "experience": [
        {
            "title": "Praktik Kerja Lapangan (PKL)",
            "organization": "Bidang Komunikasi dan Informasi Publik",
            "detail": "Bagian siaran radio. Deskripsi tugas spesifik dapat ditambahkan sesuai kegiatan yang benar-benar dilakukan.",
            "period": "[Tambahkan periode PKL jika diperlukan]",
        }
    ],
    "project_title": "Aplikasi Pengelolaan Bahan Baku Berbasis Website",
    "project_client": "Restoran Unagi dan Udang Alam Kreo",
    "project_description": (
        "Proyek perkuliahan untuk merancang aplikasi berbasis website yang mendukung "
        "pengelolaan stok bahan baku restoran. Detail teknologi, peran pribadi, dan "
        "status penyelesaian dapat ditambahkan sesuai fakta."
    ),
    "training": [
        {
            "title": "Sertifikat pelatihan",
            "provider": "[Tambahkan nama pelatihan/penyelenggara]",
            "year": "[Tambahkan tahun]",
            "note": "Informasi sertifikat perlu dilengkapi agar dapat dicantumkan secara akurat."
        }
    ],
    "achievements": [],  # Tambahkan hanya jika ada prestasi yang terverifikasi.
    "portfolio_url": "",  # Opsional: tautan proyek yang dapat diakses publik
    "linkedin_url": "",   # Opsional: tautan LinkedIn
}

st.set_page_config(
    page_title=f"E-CV | {PROFILE['name']}",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
:root { --navy:#163A63; --blue:#2463A6; --pale:#F2F7FC; --ink:#172B43; --muted:#63758A; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background:linear-gradient(180deg,#F4F8FC 0%,#FFFFFF 68%); color:var(--ink); }
.block-container { max-width:1000px; padding-top:2rem; padding-bottom:3rem; }
.hero { background:linear-gradient(120deg,#163A63 0%,#2463A6 72%,#4C8BC8 100%); color:white;
        border-radius:24px; padding:34px 36px; box-shadow:0 14px 36px rgba(22,58,99,.15); }
.eyebrow { font-size:.72rem; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:#C9E2FA; }
.hero h1 { font-family:'Playfair Display',serif; font-size:clamp(2rem,5vw,3.4rem); line-height:1.08;
           margin:.55rem 0 .65rem; color:white; }
.hero p { color:#EAF3FC; margin:.25rem 0; }
.pill { display:inline-block; border:1px solid rgba(255,255,255,.35); border-radius:999px;
        padding:7px 12px; margin-top:14px; font-size:.82rem; color:white; }
.metric { background:white; border:1px solid #DCE8F4; border-radius:18px; padding:20px; min-height:112px; }
.metric .label { color:#6A7D91; font-size:.8rem; margin-bottom:8px; }
.metric .value { color:#163A63; font-weight:700; font-size:1.1rem; }
.section-title { font-family:'Playfair Display',serif; color:#163A63; font-size:1.6rem; margin:1rem 0 .2rem; }
.section-sub { color:#63758A; font-size:.92rem; margin-bottom:1rem; }
.panel { background:white; border:1px solid #DFEAF5; border-radius:18px; padding:22px 24px; margin-bottom:12px; }
.project-tag { display:inline-block; background:#EAF3FC; color:#1F5A91; padding:5px 10px; border-radius:999px; font-size:.78rem; }
.small-muted { color:#63758A; font-size:.88rem; }
a { color:#2463A6 !important; }
footer { visibility:hidden; }
@media (max-width:640px) {
 .block-container { padding-left:1rem; padding-right:1rem; padding-top:1rem; }
 .hero { padding:25px 22px; border-radius:18px; }
 .panel { padding:18px; }
}
</style>
""", unsafe_allow_html=True)

def p(text, style):
    """Escape text before putting it into a PDF paragraph."""
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), style)

def make_pdf(profile):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer, pagesize=A4, rightMargin=1.8*cm, leftMargin=1.8*cm,
        topMargin=1.7*cm, bottomMargin=1.7*cm
    )
    navy = colors.HexColor("#163A63")
    blue = colors.HexColor("#2463A6")
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CVName", parent=styles["Title"], fontName="Helvetica-Bold",
                              fontSize=25, leading=29, textColor=navy, alignment=TA_LEFT, spaceAfter=5))
    styles.add(ParagraphStyle(name="CVHead", parent=styles["Normal"], fontSize=10, leading=15,
                              textColor=blue, spaceAfter=7))
    styles.add(ParagraphStyle(name="CVSection", parent=styles["Heading2"], fontSize=13, leading=16,
                              textColor=navy, spaceBefore=12, spaceAfter=5))
    styles.add(ParagraphStyle(name="CVBody", parent=styles["BodyText"], fontSize=9.2, leading=13,
                              textColor=colors.HexColor("#25384D"), spaceAfter=4))
    styles.add(ParagraphStyle(name="CVSmall", parent=styles["BodyText"], fontSize=8.2, leading=11,
                              textColor=colors.HexColor("#63758A"), spaceAfter=3))
    story = [
        p(profile["name"], styles["CVName"]),
        p(f'{profile["headline"]} · {profile["campus"]}', styles["CVHead"]),
        p(f'Email: {profile["email"]} | {profile["semester"]}', styles["CVBody"]),
        p("PROFIL DIRI", styles["CVSection"]),
        p(profile["about"], styles["CVBody"]),
        p("PENDIDIKAN", styles["CVSection"]),
    ]
    for item in profile["education"]:
        story.append(p(f'{item["institution"]} — {item["program"]} ({item["period"]})', styles["CVBody"]))
    story.extend([p("KEAHLIAN", styles["CVSection"]),
                  p("Teknis: " + ", ".join(profile["technical_skills"]), styles["CVBody"]),
                  p("Nonteknis: " + ", ".join(profile["soft_skills"]), styles["CVBody"]),
                  p("PENGALAMAN", styles["CVSection"])])
    for item in profile["experience"]:
        story.extend([
            p(item["title"] + " — " + item["organization"], styles["CVBody"]),
            p(item["detail"], styles["CVBody"]),
            p(item["period"], styles["CVSmall"]),
        ])
    story.extend([
        p("PROYEK DAN PORTOFOLIO", styles["CVSection"]),
        p(profile["project_title"], styles["CVBody"]),
        p(profile["project_client"], styles["CVSmall"]),
        p(profile["project_description"], styles["CVBody"]),
        p("PELATIHAN DAN SERTIFIKASI", styles["CVSection"]),
    ])
    for item in profile["training"]:
        story.extend([
            p(item["title"] + " — " + item["provider"], styles["CVBody"]),
            p(item["year"] + ". " + item["note"], styles["CVSmall"]),
        ])
    if profile["achievements"]:
        story.append(p("PRESTASI", styles["CVSection"]))
        story.extend(p(item, styles["CVBody"]) for item in profile["achievements"])
    story.extend([
        p("KONTAK PROFESIONAL", styles["CVSection"]),
        p(profile["email"], styles["CVBody"]),
    ])
    if profile["linkedin_url"]:
        story.append(p("LinkedIn: " + profile["linkedin_url"], styles["CVSmall"]))
    if profile["portfolio_url"]:
        story.append(p("Portofolio: " + profile["portfolio_url"], styles["CVSmall"]))
    story.append(Spacer(1, 8))
    story.append(p("Catatan: Lengkapi teks dalam tanda kurung siku dan periksa semua data sebelum CV dibagikan.", styles["CVSmall"]))
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()

# Optional photo upload. Uploaded image is shown for the current session.
photo = st.sidebar.file_uploader("Tambahkan foto profil (opsional)", type=["png", "jpg", "jpeg"])
if photo:
    st.sidebar.image(photo, caption="Foto profil", use_container_width=True)

st.markdown(f"""
<div class="hero">
  <div class="eyebrow">Digital Curriculum Vitae</div>
  <h1>{PROFILE['name']}</h1>
  <p><strong>{PROFILE['headline']}</strong></p>
  <p>{PROFILE['campus']}</p>
  <span class="pill">Belajar · Berkembang · Berkarya</span>
</div>
""", unsafe_allow_html=True)

st.write("")
left, right = st.columns([1, 1.6], gap="medium")
with left:
    if photo:
        st.image(photo, caption=PROFILE["name"], use_container_width=True)
    else:
        st.markdown("""
        <div class="metric">
          <div class="label">FOTO PROFIL</div>
          <div class="value">Tambahkan foto</div>
          <div class="small-muted">Gunakan unggah foto di panel kiri (opsional).</div>
        </div>
        """, unsafe_allow_html=True)
with right:
    st.markdown(f"""
    <div class="metric">
      <div class="label">PENDIDIKAN SAAT INI</div>
      <div class="value">{PROFILE['semester']}</div>
      <div class="small-muted" style="margin-top:7px">{PROFILE['campus']}</div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    <div class="metric">
      <div class="label">KEAHLIAN</div>
      <div class="value">Canva · Komunikasi · Kerja sama tim</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.download_button(
    "⬇️ Unduh CV dalam PDF",
    data=make_pdf(PROFILE),
    file_name="CV_Faisal_Yusuf.pdf",
    mime="application/pdf",
    type="primary",
)

st.markdown('<div class="section-title">01 / Tentang Saya</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Ringkasan profil dan minat saya.</div>', unsafe_allow_html=True)
st.markdown(f'<div class="panel">{PROFILE["about"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">02 / Pendidikan</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Riwayat pendidikan yang relevan.</div>', unsafe_allow_html=True)
for item in PROFILE["education"]:
    st.markdown(f"""
    <div class="panel">
      <div class="project-tag">PENDIDIKAN</div>
      <h4 style="color:#2463A6;margin:.8rem 0 .3rem">{item['institution']}</h4>
      <strong>{item['program']}</strong><br/>
      <span class="small-muted">{item['period']}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">03 / Keahlian</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Keahlian teknis dan nonteknis yang dicantumkan berdasarkan informasi yang diberikan.</div>', unsafe_allow_html=True)
skill_cols = st.columns(2)
with skill_cols[0]:
    st.markdown('<div class="panel"><div class="project-tag">TEKNIS</div><h4 style="color:#163A63">Canva</h4><p class="small-muted">Desain dan pembuatan konten digital.</p></div>', unsafe_allow_html=True)
with skill_cols[1]:
    st.markdown('<div class="panel"><div class="project-tag">NONTEKNIS</div><h4 style="color:#163A63">Komunikasi</h4><h4 style="color:#163A63">Kerja sama tim</h4></div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">04 / Pengalaman</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Pengalaman praktik kerja lapangan.</div>', unsafe_allow_html=True)
for item in PROFILE["experience"]:
    st.markdown(f"""
    <div class="panel">
      <div class="project-tag">PENGALAMAN</div>
      <h3 style="color:#163A63;margin:.8rem 0 .35rem">{item['title']}</h3>
      <strong>{item['organization']}</strong>
      <p class="small-muted" style="margin-top:.7rem">{item['detail']}</p>
      <p class="small-muted">{item['period']}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">05 / Proyek dan Portofolio</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Proyek perkuliahan dan karya digital.</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="panel">
  <div class="project-tag">PROYEK PERKULIAHAN</div>
  <h3 style="color:#163A63;margin:.8rem 0 .35rem">{PROFILE['project_title']}</h3>
  <strong>{PROFILE['project_client']}</strong>
  <p class="small-muted" style="margin-top:.7rem">{PROFILE['project_description']}</p>
</div>
""", unsafe_allow_html=True)
if PROFILE["portfolio_url"]:
    st.markdown(f'[Lihat portofolio proyek]({PROFILE["portfolio_url"]})')

st.markdown('<div class="section-title">06 / Pelatihan dan Sertifikasi</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Lengkapi nama dan penyelenggara sertifikat agar informasinya akurat.</div>', unsafe_allow_html=True)
for item in PROFILE["training"]:
    st.markdown(f"""
    <div class="panel">
      <div class="project-tag">SERTIFIKASI</div>
      <h4 style="color:#163A63;margin:.7rem 0 .3rem">{item['title']}</h4>
      <strong>{item['provider']}</strong>
      <p class="small-muted">{item['year']}</p>
      <p class="small-muted">{item['note']}</p>
    </div>
    """, unsafe_allow_html=True)

if PROFILE["achievements"]:
    st.markdown('<div class="section-title">Prestasi</div>', unsafe_allow_html=True)
    for item in PROFILE["achievements"]:
        st.markdown(f'<div class="panel">{item}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-title">07 / Kontak Profesional</div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="panel">
  <strong>Email</strong><br/>
  <a href="mailto:{PROFILE['email']}">{PROFILE['email']}</a>
</div>
""", unsafe_allow_html=True)
if PROFILE["linkedin_url"]:
    st.markdown(f'[LinkedIn]({PROFILE["linkedin_url"]})')

st.markdown("---")
st.caption("E-CV • Digital Kreatif | Periksa kembali semua informasi sebelum membagikan tautan publik.")
