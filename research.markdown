---
layout: single
title: Research
permalink: /research/
---

<style>
.left-photo-block {
    display: flex;
    align-items: flex-start;
    gap: 40px; 
    margin: 40px 0;
}

.left-photo-block img {
    max-width: 500px; 
    height: auto;
    border-radius: 8px;
    flex-shrink: 0;
}

/* Stack on small screens */
@media (max-width: 600px) {
  .left-photo-block {
    flex-direction: row;
  }
}
</style>


<style>
.figure-text-block {
  margin: 30px auto;
}

.figure-text-block img {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 0 auto 15px auto;  /* centers image + space below */
  border-radius: 8px;        /* optional */
}

.figure-text-block .text {
  line-height: 1.6;
}
</style>

## Big picture
* Getting the most out of materials systems requires an accurate understanding of their properties and responses to stimuli.
* Our group is broadly interested in developing state-of-the-art theoretical and computational tools to better understand a variety of materials systems. 
* We aim to develop accurate and efficient first-principles methods along with corresponding high-performance computer codes.  

## Recent examples 

### Exciton-polaritons 

<div class="figure-text-block">
 <img src="/assets/images/EP_1.png" alt = "Exciton-polaritons">
 <div>
   We <a href="https://arxiv.org/abs/2503.13613">developed</a> a robust theoretical framework to naturally capture light-matter interactions based on the standard methods of many-body perturbation theory (MBPT).
   In particular, we use an interacting Green's function formalism to incorporate coupling of excitons with photons into a "polaritonic" Bethe-Salpeter equation (pBSE). 
   Our method captures the strong hybridization of excitons (matter) and photons (light) at small center-of-mass momenta, even providing excellent agreement with experimentally determined dispersions.
   We are able to quantify the extent of light-matter hybridization as well as the strong spatial localization of our lowest exciton solution due to the hybridization with light.
   Our framework is numerically efficient, only requiring a small calculation on top of standard BSE computations.  
 </div>
</div>

### Defects in diamond

<div class="figure-text-block">
 <img src="/assets/images/PJT_1.png" alt = "Product Jahn-Teller">
 <div> 
  We explored two sets of novel defect classes in diamond: the <a href="https://journals.aps.org/prb/abstract/10.1103/PhysRevB.102.195206?ft=1">negatively-charged group III split-vacancy defects</a>
  (AlV<sup>-</sup>, GeV<sup>-</sup>, InV<sup>-</sup>, TlV<sup>-</sup>) and the 
  <a href="https://www.nature.com/articles/s41535-020-00281-7">neutral group IV split-vacancy defects</a> 
  (SiV<sup>0</sup>, GeV<sup>0</sup>, SnV<sup>0</sup>, PbV<sup>0</sup>). 
  Both of these classes are <i>iso</i>electronic, meaning their electronic configurations are the same. 
  In particular, the excited-state electronic configuration is composed of two doubly-degenerate states with unequal occupations in each. 
  This results in a pair of symmetry-lowering Jahn-Teller distortions occuring simultaneously, otherwise known as a product Jahn-Teller effect.

  We use first-principles hybrid density-functional theory calculations to capture these distortions, which are energetically significant (100s of meVs).
  Only by including these distortions are we able to accurately predict the transition energies expected in experiment. 
  Additionally, these Jahn-Teller distortions have an effect on other interactions in the defect, including the spin-orbit coupling. 
  We predict that the naively-predicted spin-orbit splitting is <i>quenched</i> by almost two order of magnitude because of the Jahn-Teller physics at play.
  This fine structure detail again serves as a useful fingerprint for identifying these defects in experiment. 
 </div>
</div>


