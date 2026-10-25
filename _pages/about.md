---
permalink: /
title: "Hi, I'm Haoyao 👋"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

🎓 Ph.D. Candidate &nbsp;·&nbsp; 📊 Statistics & Data Science &nbsp;·&nbsp; 🏛 UT Arlington &nbsp;·&nbsp; 📍 Dallas, TX

I am a Ph.D. candidate in Statistics and Data Science at the **University of Texas at Arlington**, expected to graduate in summer 2027. My dissertation develops **Bayesian models for partially observed and aggregate data**.

Before the Ph.D., I spent over three years as a full time statistician in Canada. At **Cytel** (Real World Evidence and Advanced Analytics) I built oncology evidence for pharma sponsors: indirect treatment comparisons (MAIC, STC), external and synthetic control arms with Bayesian borrowing, and survival analysis. At **ERM** I built multivariate models for environmental and health risk assessments and automated reporting with Shiny and R Markdown. In summer 2026 I interned with **Novartis Advanced Quantitative Sciences**, where I built a Shiny app that tracks survival data maturity and predicts events in oncology trials.

I hold an M.Sc. in Statistics from **Simon Fraser University** (2019) and a B.Sc. in Applied Statistics with Distinction from the **University of Toronto** (2017).

Research Interests
======

<div class="interest-grid">
  <div class="interest-card"><div class="interest-icon">🎲</div><h3>Bayesian Hierarchical Models</h3><p>MCMC based inference for partially observed and aggregate data, including Bayesian aggregation of peer and self rankings.</p></div>
  <div class="interest-card"><div class="interest-icon">🧪</div><h3>Comparative Effectiveness</h3><p>Indirect treatment comparisons (MAIC, STC) and external control arms for oncology submissions.</p></div>
  <div class="interest-card"><div class="interest-icon">🔁</div><h3>Bayesian Borrowing</h3><p>Augmenting external and synthetic control arms with historical information, and the variance versus bias trade offs involved.</p></div>
  <div class="interest-card"><div class="interest-icon">⏳</div><h3>Survival Analysis</h3><p>Survival models in oncology trials and a Bayesian predictive index for survival data analysis readiness.</p></div>
  <div class="interest-card"><div class="interest-icon">📈</div><h3>Simulation and Power</h3><p>Monte Carlo evaluation of methods and simulation based power analysis for GLMMs and GAMMs.</p></div>
  <div class="interest-card"><div class="interest-icon">🧰</div><h3>Statistical Software</h3><p>R, Shiny and R Markdown tooling for reproducible analyses and interactive reporting; working SAS and Python.</p></div>
</div>

Latest News
======

<ul class="news-list">
{% for post in site.posts limit:8 %}
  <li><span class="news-date">{{ post.date | date: "%b %Y" }}</span> <a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>

[See all news →](/year-archive/)
