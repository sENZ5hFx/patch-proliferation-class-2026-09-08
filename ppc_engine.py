#!/usr/bin/env python3
"""Patch-Proliferation Class (PPC) engine — 2026-09-08.

Research-stage classification. Not a physical discovery, not peer review, not a patent.

After subtracting thirteen archived classes, remaining unknown:
  a coordinate that has lost majority belief (or never had a positive-identity
  majority) keeps absorbing residuals by adding unobservable degrees of freedom
  that leave the operational pipeline intact.

This is not Transducer-Absence (naming a missing converter "dark").
This is the *next* move: couple two unsolveds, or add a patch parameter,
so the unloved coordinate can keep reducing data.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

Status = Literal["STRUCTURAL_GAP", "PENALIZED", "KILLED", "ZEROED"]

PRIOR_CLASSES = [
    ("Dark Biosphere Hypothesis", "2026-05-14", "networked subsurface life as architecture"),
    ("Cosmic-Bio Resonance", "2026-05-14", "cosmic structure as downward biological constraint"),
    ("Undersampling", "2026-08-03", "WHERE we look"),
    ("Deep-biosphere-as-space-prior", "2026-08-14", "Earth's dark interior as analog for icy moons"),
    ("Ritual Nyquist Law", "2026-08-27", "ritualized sampling rates"),
    ("Transducer-Absence Class (TAC)", "2026-08-28", "signal detected, layer named dark, converter not located"),
    ("Cadence Mismatch", "2026-08-29", "sampling cadence vs process cadence"),
    ("Named-Cause Residual (NCR) + Initiation–Maintenance Split", "2026-08-30", "official explanation real but insufficient"),
    ("Failed-Adjudication Class (FAC)", "2026-08-31", "a dispute that never reaches a verdict"),
    ("Clock-Incommensurability Class (CIC)", "2026-09-01", "observation cadence cannot resolve process cadence"),
    ("Join-Absence Class (JAC)", "2026-09-02", "two ledgers share a channel; cartesian product never the object"),
    ("Interscale-Operator Absence Class (IOA)", "2026-09-04", "two scales of one named process; transfer function unowned"),
    ("Destructive-Inquiry Class (DIC)", "2026-09-06", "object already seen; closing protocol consumes it"),
]

ZERO_CONTROLS = [
    "nodule dark oxygen (Sweetman 2024 + Editor's Note 8 Apr 2026) — FAC+TAC, do not load-bear",
    "magnetoreceptor cell — TAC",
    "inner-core state as NCR primary — do not reclaim as NCR; may be scored as PPC only if the move is a patch parameter",
    "Hubble tension as FAC primary — do not reclaim the tension; patches *to* the tension may be PPC",
    "dark matter / dark energy identity — TAC",
    "consciousness — archive-refused",
    "universal dark-fraction law — killed JAC",
    "UPE-as-communication — killed",
    "wood-wide web Type I — IOA",
    "K2-18b DMS-as-life",
    "Cry4 in-vitro to heading — IOA Type III",
    "QG as solution to H0",
    "Cosmic-Bio Resonance / Dark Biosphere — not reclaimed",
    "hadal Animalia incerta sedis — DIC primary, not PPC",
    "ice-core archive — DIC secondary, not PPC",
]


@dataclass
class Instance:
    id: str
    realm: str
    name: str
    claim: str
    source: str
    freshness: float  # 0-1, 1 = 2026-09-07/08 lock
    sourced: float  # 0-1 primary-source quality
    falsifiable: float  # 0-1
    not_prior: float  # 0-1 distinctness from 13 classes
    pipeline_intact: float  # 0-1 does the patch leave the coordinate running
    unobservable_dof: float  # 0-1 extra DOF is unobservable by construction
    majority_lost: float  # 0-1 coordinate lacks majority OR successor vacuum
    penalty: float  # 0-1 subtracted
    kill_reason: str | None = None
    overlap: str | None = None
    discriminator: str = ""
    sense: str = ""

    @property
    def raw(self) -> float:
        # Weighted structural score. Heuristic, not a measurement of nature.
        w = (
            10.0 * self.not_prior
            + 8.0 * self.pipeline_intact
            + 8.0 * self.unobservable_dof
            + 7.0 * self.majority_lost
            + 6.0 * self.falsifiable
            + 5.0 * self.sourced
            + 4.0 * self.freshness
        )
        return round(w * (1.0 - self.penalty), 2)

    @property
    def status(self) -> Status:
        if self.kill_reason and self.penalty >= 1.0:
            return "ZEROED" if "ZERO" in self.kill_reason.upper() or "zero" in (self.kill_reason or "") else "KILLED"
        if self.penalty >= 1.0:
            return "KILLED"
        if self.penalty >= 0.35:
            return "PENALIZED"
        if self.raw >= 18.0 and self.not_prior >= 0.7:
            return "STRUCTURAL_GAP"
        if self.raw >= 12.0:
            return "PENALIZED"
        return "KILLED"


def catalog() -> list[Instance]:
    return [
        Instance(
            id="DARK_DIMENSION",
            realm="Outer Space",
            name="Dark dimension coupling dark energy × dark matter",
            claim=(
                "DESI 2024/2025 prefers evolving (weakening) dark energy. "
                "Rather than retire Λ as the coordinate, a 2019 'dark dimension' "
                "scenario (Obied, Vafa, Bedroya, Wu 2025) absorbs both DM and DE "
                "residuals by adding an extra compact dimension whose size sets both. "
                "WIRED/Quanta coverage 2026-09-07. The pipeline (ΛCDM reduction of "
                "BAO+CMB+SNe) stays intact; the extra DOF is unobservable by construction."
            ),
            source="Obied, Vafa, Bedroya, Wu 2025; WIRED 2026-09-07; DESI DR2 2025",
            freshness=0.95,
            sourced=0.85,
            falsifiable=0.7,
            not_prior=0.88,
            pipeline_intact=0.95,
            unobservable_dof=0.92,
            majority_lost=0.8,
            penalty=0.12,  # extra-dimension prior art (2019); class is the *move*, not the dimension
            overlap="TAC owns DM/DE identity. PPC is the coupling-as-patch, not the identity.",
            discriminator=(
                "Pre-register a unique dark-dimension prediction (e.g. a specific "
                "w(z) shape AND a DM coupling scale) that ΛCDM+w0wa cannot mimic. "
                "If Rubin/Euclid/Roman fit w0wa without the extra dimension, PPC holds "
                "and the patch failed as successor. If the unique prediction is confirmed, "
                "PPC is wrong — it became a successor coordinate."
            ),
            sense="Vision (survey geometry) / Time (expansion history)",
        ),
        Instance(
            id="LCDM_BELIEF_SPLIT",
            realm="Outer Space",
            name="ΛCDM operational default after majority-loss (physicists survey)",
            claim=(
                "Afshordi, Halper, Rini, Schirber, arXiv:2605.11058 (10 May 2026), "
                "press 2026-09-08: ΛCDM failed to gain majority support among physicists "
                "surveyed. Inflation 51% (bare majority). String 19%, LQG 12%, gravity "
                "unquantized 18%. DM: 21% combination, 17% low-mass particles, 12% modified "
                "gravity. Authors: 'scientific truth is not decided by a vote.' Sample is "
                "'physicists worldwide' — not demonstrated to be working cosmologists."
            ),
            source="arXiv:2605.11058; SciTechDaily / Waterloo / Perimeter 2026-09-08",
            freshness=1.0,
            sourced=0.8,
            falsifiable=0.55,
            not_prior=0.82,
            pipeline_intact=0.9,
            unobservable_dof=0.4,  # the split itself is not a DOF; it licenses DOF
            majority_lost=0.85,
            penalty=0.38,  # population error: physicists ≠ cosmologists; survey May not Sept; vote ≠ ontology
            overlap="FAC owns Hubble-tension verdict failure. This is belief vs pipeline, not a discriminator.",
            discriminator=(
                "Re-cut the survey on self-identified cosmologists only. If ΛCDM then "
                "has majority, this instance dies (population error). If it still lacks "
                "majority, measure the fraction of 2026 DESI/Euclid/Rubin papers whose "
                "headline result is reported as a ΛCDM residual. PPC holds if that "
                "fraction stays high while belief-majority stays lost."
            ),
            sense="Time (who still reduces to the coordinate)",
        ),
        Instance(
            id="EARLY_DARK_ENERGY",
            realm="Outer Space",
            name="Early dark energy / extra neutrinos as H0 patches",
            claim=(
                "Hubble tension (local H0 73.50±0.81, H0DN 2026-04 vs Planck ~67) remains "
                "FAC. EDE, extra Neff, and similar pre-recombination patches add DOF to "
                "keep the ΛCDM pipeline. They are the industry of residue-absorbers."
            ),
            source="H0DN A&A April 2026; CosmoVerse White Paper 2025; Poulin EDE literature",
            freshness=0.55,
            sourced=0.85,
            falsifiable=0.75,
            not_prior=0.45,  # heavy FAC overlap
            pipeline_intact=0.9,
            unobservable_dof=0.7,
            majority_lost=0.7,
            penalty=0.55,
            overlap="FAC primary for Hubble tension. PPC only on the patch-industry, not the tension.",
            discriminator="If a patch is required by independent probes (not just H0), it is a successor. If it only fits H0 and worsens S8, it is PPC.",
            sense="Time",
        ),
        Instance(
            id="IMF_EXPORT",
            realm="Outer Space",
            name="Milky Way IMF exported to z≳5 galaxies",
            claim=(
                "JWST 'impossibly early' massive galaxies assumed a MW-like IMF. "
                "van Dokkum et al. / Nature Astronomy 2026-08-18: oldest galaxy "
                "(z_form>5) most bottom-heavy; masses may rise by ~4±1. A 2026-07-24 "
                "ApJL paper claims the crisis is a reionization degeneracy, not mass. "
                "Two patches compete to save the formation-efficiency coordinate."
            ),
            source="Nature Astronomy 2026-08-18; ApJL 1006 L41 (2026-07-24)",
            freshness=0.7,
            sourced=0.9,
            falsifiable=0.85,
            not_prior=0.62,
            pipeline_intact=0.8,
            unobservable_dof=0.35,  # IMF is in principle observable via spectra
            majority_lost=0.5,
            penalty=0.36,  # field already owns 'IMF varies' (Nature Astronomy 2026); observable → EPC not PPC
            overlap="Closer to Exported-Prior (iterate). Observable, so weak unobservable-DOF.",
            discriminator="JWST Cycles 3–4 spectra of the same objects: if bottom-heavy IMF is measured, the 'crisis' was calibration export (EPC), not new physics. If IMF is MW-like and masses stay high, PPC/EPC both fail and formation physics must change.",
            sense="Vision",
        ),
        Instance(
            id="IRON_MELT_EXPORT",
            realm="Land / Deep Earth",
            name="Iron melting-curve geometry exported to the core",
            claim=(
                "New-core paradox: field ≥4 Gyr, inner core often modeled ~0.5 Gyr. "
                "Goldschmidt 2026: iron melts >1000°C cooler under corelike conditions "
                "than longstanding curves. The 'pure iron, old melting curve' coordinate "
                "is patched by light elements (C ~3.8% for nucleation, Oxford 2025 Nature "
                "Communications) rather than retired."
            ),
            source="Science/AAAS Goldschmidt report; Nature Communications 2025 (Fe-C nucleation)",
            freshness=0.65,
            sourced=0.8,
            falsifiable=0.7,
            not_prior=0.6,
            pipeline_intact=0.85,
            unobservable_dof=0.4,
            majority_lost=0.45,
            penalty=0.4,  # NCR overlap on inner-core composition; archive said do not reclaim inner-core as NCR primary
            overlap="NCR owns 'named cause insufficient'. PPC only if adding C/O/Si/S is a patch that saves the iron-coordinate rather than a measurement.",
            discriminator="Independent melting-curve labs must agree on the cooler curve. If they do, the paradox was calibration export (EPC), not a new energy source. If they do not, PPC does not apply (it is FAC).",
            sense="Magnetism / Pressure",
        ),
        Instance(
            id="HYDROGEN_BUDGET_PATCH",
            realm="Deep Ocean",
            name="Kunlun hydrogen field as patch to the global abiotic H2 budget",
            claim=(
                "Kunlun hydrothermal system (Science Advances 2025-08-08): estimated "
                "4.8e11 mol/yr H2, ≥5% of global submarine abiotic hydrogen from one field. "
                "The 'diffuse, well-mixed abiotic hydrogen' coordinate is patched by adding "
                "a giant point source rather than rebuilding the inventory method. Doldrums "
                "hybrid vents (Schmidt / MBARI, reported 2026-09-08) further imply transform "
                "faults are missing terms, not extra patches."
            ),
            source="EurekAlert/IOCAS 2025-08-08; Marine Technology News 2026-09-08 (Doldrums)",
            freshness=0.9,
            sourced=0.85,
            falsifiable=0.65,
            not_prior=0.55,
            pipeline_intact=0.7,
            unobservable_dof=0.2,
            majority_lost=0.35,
            penalty=0.42,  # Undersampling of vents is the simpler class; Doldrums = look more
            overlap="Undersampling (more vents). PPC only on the *budget equation* that absorbs each new field as a patch term.",
            discriminator="If a systematic transform-fault survey predicts Kunlun-class flux a priori, this is undersampling. If each new field is added post hoc to keep a pre-2015 budget form, PPC holds.",
            sense="Chemical",
        ),
        Instance(
            id="WHALE_VOWEL_EXPORT",
            realm="Animal Behavior",
            name="Human phonetic inventory exported to sperm-whale codas",
            claim=(
                "Project CETI 2025–2026: sperm-whale clicks described as vowels, "
                "diphthongs, rubato, ornamentation — terms from human phonology. "
                "The finding of combinatorial structure is sourced. The *labels* are "
                "an exported prior. Danger: dismissing a real homology. Scored as EPC "
                "iterate, weak PPC (the coordinate 'animal communication is not language' "
                "is being patched by importing our phonology rather than building theirs)."
            ),
            source="Project CETI; Proceedings B 2026-04; NYT 2025-11-23; Guardian 2026-04-15",
            freshness=0.6,
            sourced=0.85,
            falsifiable=0.5,
            not_prior=0.5,
            pipeline_intact=0.6,
            unobservable_dof=0.15,
            majority_lost=0.3,
            penalty=0.5,
            overlap="EPC iterate. Not TAC. Consciousness refused — do not smuggle sentience.",
            discriminator=(
                "Hold out a naive listener (no human-phonetic labels) + a model with "
                "whale-native features only. If combinatorial structure survives without "
                "vowel/rubato labels, the structure is real and EPC was about naming. "
                "If structure collapses, PPC/EPC holds: we patched 'not language' by "
                "importing ours."
            ),
            sense="Hearing",
        ),
        Instance(
            id="NAUTILUS_EXPORT",
            realm="Animal Behavior",
            name="Coleoid sentience criteria exported to nautilus",
            claim=(
                "Schnell 2026 Biological Reviews: octopus/cuttlefish meet 6/8 sentience "
                "criteria; nautilus 1/8, and every miss is insufficient evidence, never "
                "a demonstrated fail. The coleoid coordinate is being used as the "
                "reduction target for a lineage that diverged ~500 Myr earlier."
            ),
            source="Schnell et al., Biological Reviews 2026 (doi 10.1002/brv.70125)",
            freshness=0.85,
            sourced=0.9,
            falsifiable=0.8,
            not_prior=0.48,
            pipeline_intact=0.55,
            unobservable_dof=0.1,
            majority_lost=0.2,
            penalty=0.55,  # Undersampling of nautilus research; authors already say this
            overlap="Undersampling. Authors own the gap. Not a patch to save a coordinate.",
            discriminator="A nautilus-first criterion set, pre-registered, that is allowed to return 'unknown' without importing coleoid scores.",
            sense="Touch / Chemical",
        ),
        Instance(
            id="PLACEBO_PHARM",
            realm="Human Neuroscience",
            name="Placebo as residual patch on the drug-coordinate",
            claim=(
                "Pharmacology's operational coordinate is molecule→receptor→effect. "
                "Placebo/nocebo residuals are absorbed as 'context effects' without "
                "retiring the coordinate. Prior art is large. Consciousness refused."
            ),
            source="Standard medical literature; not 2026-fresh as a class object",
            freshness=0.1,
            sourced=0.7,
            falsifiable=0.4,
            not_prior=0.25,
            pipeline_intact=0.8,
            unobservable_dof=0.3,
            majority_lost=0.2,
            penalty=0.7,
            overlap="NCR + prior art. Consciousness adjacent — do not load-bear.",
            discriminator="Not run this session.",
            sense="Chemical / Time",
        ),
        Instance(
            id="DARK_OXYGEN",
            realm="Deep Ocean",
            name="Nodule 'dark oxygen' as abiotic O2 patch",
            claim=(
                "Sweetman et al. Nature Geoscience 2024. Editor's Note 8 Apr 2026. "
                "Frontiers Marine Science 2025 critique. Re-analysis 2026: O2 rose "
                "regardless of nodule presence. Archive ZERO. Do not load-bear."
            ),
            source="Nature Geoscience 2024 + Editor's Note 2026-04-08; Front. Mar. Sci. 2025",
            freshness=0.4,
            sourced=0.9,
            falsifiable=0.9,
            not_prior=0.1,
            pipeline_intact=0.2,
            unobservable_dof=0.2,
            majority_lost=0.2,
            penalty=1.0,
            kill_reason="ZEROED by archive (FAC+TAC). Contested; unreplicated; possible artefact.",
            overlap="ZERO control.",
            discriminator="Not run. Independent replication with pre-registered nodule-absent controls would be FAC, not PPC.",
            sense="Chemical",
        ),
        Instance(
            id="HADAL_INCERTA",
            realm="Deep Ocean",
            name="Hadal Animalia incerta sedis",
            claim="Filmed twice to 9,137 m. Identity closed only by consuming capture. DIC primary 2026-09-06.",
            source="Jamieson / Swanborn et al. Biodiversity Data Journal 2026",
            freshness=0.4,
            sourced=0.9,
            falsifiable=0.8,
            not_prior=0.05,
            pipeline_intact=0.0,
            unobservable_dof=0.0,
            majority_lost=0.0,
            penalty=1.0,
            kill_reason="KILLED as PPC — already DIC primary. Not a patch to a coordinate.",
            overlap="DIC.",
            discriminator="See 2026-09-06 session.",
            sense="Vision / Pressure",
        ),
        Instance(
            id="UNIFORMITARIAN_PATCH",
            realm="Land Ecosystems",
            name="Lost seafloor / stalled slab as patch to simple subduction",
            claim=(
                "Tomography candidate for 'lost seafloor' stalled in the mantle "
                "transition zone east of the East Pacific Rise. Each anomalous slab "
                "is added to keep the simple-subduction coordinate rather than "
                "changing how plates are allowed to founder."
            ),
            source="Interesting Engineering 2025 roundup; tomography literature late 2024",
            freshness=0.35,
            sourced=0.55,
            falsifiable=0.5,
            not_prior=0.4,
            pipeline_intact=0.7,
            unobservable_dof=0.45,
            majority_lost=0.25,
            penalty=0.5,
            overlap="NCR / Undersampling of mantle.",
            discriminator="If geodynamic models predicted stall locations before the tomography, not PPC.",
            sense="Pressure / Time",
        ),
        Instance(
            id="CONSCIOUSNESS",
            realm="Human Neuroscience",
            name="Hard problem of consciousness",
            claim="Archive-refused. Not scored as PPC.",
            source="archive control",
            freshness=0.0,
            sourced=0.0,
            falsifiable=0.0,
            not_prior=0.0,
            pipeline_intact=0.0,
            unobservable_dof=0.0,
            majority_lost=0.0,
            penalty=1.0,
            kill_reason="KILLED — archive refused. Do not smuggle via NCC 'patches'.",
            overlap="Refused.",
            discriminator="None.",
            sense="—",
        ),
        Instance(
            id="POPIII_PATCH",
            realm="Outer Space",
            name="Pop III still unseen; metal-line diagnostics as patch",
            claim=(
                "No pristine Pop III stars known as of mid-2026 (Siegel; CSI Sesto 2026). "
                "JWST sees metal-polluted systems at highest z. New UV-metal diagnostics "
                "(ApJL 2025) select 'Pop III candidates' with >25% metal-free mass — a "
                "patch that keeps the Pop III coordinate without a metal-free object."
            ),
            source="arXiv:2607.00167 (2026-08); ApJL 2025 metal-polluted Pop III; Siegel 2025-12",
            freshness=0.75,
            sourced=0.85,
            falsifiable=0.7,
            not_prior=0.68,
            pipeline_intact=0.85,
            unobservable_dof=0.55,
            majority_lost=0.4,
            penalty=0.22,
            overlap="Undersampling of first stars is the naive class. PPC is the candidate-threshold that lets the coordinate survive without a pristine object.",
            discriminator="A pre-registered 'zero metals, He II, no AGN mimic' object. If the next three years only yield mixed-mass candidates, PPC holds. One clean Pop III galaxy kills this instance.",
            sense="Vision",
        ),
    ]


def score_ppc_instance(inst: Instance) -> dict:
    """Score one instance. Input validation + edge cases."""
    if not inst.id or not inst.realm:
        raise ValueError("id and realm are required")
    for f in (
        "freshness",
        "sourced",
        "falsifiable",
        "not_prior",
        "pipeline_intact",
        "unobservable_dof",
        "majority_lost",
        "penalty",
    ):
        v = getattr(inst, f)
        if not (0.0 <= v <= 1.0):
            raise ValueError(f"{f} must be in [0,1], got {v}")
    return {
        "id": inst.id,
        "realm": inst.realm,
        "name": inst.name,
        "status": inst.status,
        "score": inst.raw,
        "penalty": inst.penalty,
        "kill_reason": inst.kill_reason,
        "overlap": inst.overlap,
        "source": inst.source,
        "claim": inst.claim,
        "discriminator": inst.discriminator,
        "sense": inst.sense,
        "operators": {
            "not_prior": inst.not_prior,
            "pipeline_intact": inst.pipeline_intact,
            "unobservable_dof": inst.unobservable_dof,
            "majority_lost": inst.majority_lost,
            "falsifiable": inst.falsifiable,
            "sourced": inst.sourced,
            "freshness": inst.freshness,
        },
    }


def score_epc_instance(
    name: str,
    home_domain: str,
    foreign_domain: str,
    prior_valid_at_home: float,
    independently_verified_abroad: float,
    anomaly_treated_as_new_physics: float,
    field_already_owns_the_export: float,
) -> dict:
    """Iterate: Exported-Prior Class.

    A calibration valid in its home domain is used as the reduction prior in a
    foreign domain. Distinct from PPC (PPC adds unobservable DOF; EPC illegally
    exports an observable prior). Distinct from IOA (IOA is two scales of one
    named process; EPC is two different objects).
    """
    for n, v in [
        ("prior_valid_at_home", prior_valid_at_home),
        ("independently_verified_abroad", independently_verified_abroad),
        ("anomaly_treated_as_new_physics", anomaly_treated_as_new_physics),
        ("field_already_owns_the_export", field_already_owns_the_export),
    ]:
        if not (0.0 <= v <= 1.0):
            raise ValueError(f"{n} out of range")
    # If verified abroad, EPC is wrong (the prior was legal).
    # If the field already owns the export as its object, EPC is prior art.
    legality = prior_valid_at_home * (1.0 - independently_verified_abroad)
    score = round(
        12.0 * legality
        + 10.0 * anomaly_treated_as_new_physics
        + 8.0 * (1.0 - field_already_owns_the_export)
        - 14.0 * independently_verified_abroad,
        2,
    )
    if independently_verified_abroad >= 0.8:
        status: Status = "KILLED"
        why = "Prior independently verified in the foreign domain — export was legal."
    elif field_already_owns_the_export >= 0.7:
        status = "PENALIZED"
        why = "Field already owns 'the prior was exported' as the literature's object."
    elif score >= 16:
        status = "STRUCTURAL_GAP"
        why = "Illegal export still treated as new physics."
    else:
        status = "PENALIZED"
        why = "Weak EPC."
    return {
        "name": name,
        "home_domain": home_domain,
        "foreign_domain": foreign_domain,
        "status": status,
        "score": max(score, 0.0),
        "why": why,
    }


def patch_is_successor_or_mimic(
    name: str,
    unique_predictions: list[str],
    mimicable_by_existing_dof: float,
    independent_probes: int,
    unique_probe_hits: int,
    pipeline_still_lcdm: bool,
) -> dict:
    """Iterate #2: decide whether a patch is a successor coordinate or a mimic.

    A successor makes at least one prediction that existing DOF (w0wa, Neff, IMF, …)
    cannot mimic, and that prediction is tested on a probe the original residual
    did not use. A mimic only absorbs the original residual.
    """
    if not name.strip():
        raise ValueError("name required")
    if not unique_predictions:
        raise ValueError("unique_predictions must be a non-empty list of claimed unique tests")
    if not (0.0 <= mimicable_by_existing_dof <= 1.0):
        raise ValueError("mimicable_by_existing_dof in [0,1]")
    if independent_probes < 0 or unique_probe_hits < 0:
        raise ValueError("probe counts must be >= 0")
    if unique_probe_hits > independent_probes:
        raise ValueError("unique_probe_hits cannot exceed independent_probes")

    hit_rate = unique_probe_hits / independent_probes if independent_probes else 0.0
    if mimicable_by_existing_dof >= 0.8:
        verdict = "MIMIC"
        why = "Existing degrees of freedom can reproduce the residual. Patch is not a successor."
    elif hit_rate >= 0.67 and not pipeline_still_lcdm:
        verdict = "SUCCESSOR"
        why = "Unique predictions hit on independent probes and the pipeline moved."
    elif hit_rate >= 0.67 and pipeline_still_lcdm:
        verdict = "PATCH_HOLDING"
        why = "Unique hits, but data are still reduced through the old coordinate. PPC still holds."
    elif independent_probes == 0:
        verdict = "UNTESTED_PATCH"
        why = "Unique predictions are named but not yet run. Default: treat as PPC until a unique probe fires."
    else:
        verdict = "MIMIC_LEANING"
        why = "Independent probes have been run; unique hits are too few to promote the patch."

    return {
        "name": name,
        "verdict": verdict,
        "why": why,
        "unique_predictions": unique_predictions,
        "mimicable_by_existing_dof": mimicable_by_existing_dof,
        "independent_probes": independent_probes,
        "unique_probe_hits": unique_probe_hits,
        "hit_rate": round(hit_rate, 3),
        "pipeline_still_lcdm": pipeline_still_lcdm,
    }


def run() -> dict:
    instances = catalog()
    rows = [score_ppc_instance(i) for i in instances]
    rows.sort(key=lambda r: r["score"], reverse=True)

    gaps = [r for r in rows if r["status"] == "STRUCTURAL_GAP"]
    penalized = [r for r in rows if r["status"] == "PENALIZED"]
    killed = [r for r in rows if r["status"] in ("KILLED", "ZEROED")]

    epc = [
        score_epc_instance(
            "MW IMF → z≳5 galaxies",
            "Milky Way / z~0.7 massive quiescent",
            "JWST early galaxies",
            prior_valid_at_home=0.9,
            independently_verified_abroad=0.25,
            anomaly_treated_as_new_physics=0.7,
            field_already_owns_the_export=0.65,  # Nature Astronomy 2026 is the field owning it
        ),
        score_epc_instance(
            "Iron melting curve → inner core temperature",
            "diamond-anvil geometry A",
            "outer-core dynamo energy budget",
            prior_valid_at_home=0.7,
            independently_verified_abroad=0.35,
            anomaly_treated_as_new_physics=0.6,
            field_already_owns_the_export=0.55,
        ),
        score_epc_instance(
            "Human phonology → sperm-whale codas",
            "human speech",
            "Physeter macrocephalus click trains",
            prior_valid_at_home=1.0,
            independently_verified_abroad=0.4,  # combinatorial structure may be real
            anomaly_treated_as_new_physics=0.5,
            field_already_owns_the_export=0.4,
        ),
        score_epc_instance(
            "Coleoid sentience battery → nautilus",
            "octopus/cuttlefish",
            "Nautilus",
            prior_valid_at_home=0.85,
            independently_verified_abroad=0.1,
            anomaly_treated_as_new_physics=0.2,
            field_already_owns_the_export=0.85,  # Schnell already says unknown
        ),
    ]
    epc.sort(key=lambda r: r["score"], reverse=True)

    mimic_tests = [
        patch_is_successor_or_mimic(
            name="Dark dimension (Obied/Vafa/Bedroya/Wu)",
            unique_predictions=[
                "specific w(z) shape not mimicable by w0wa",
                "DM coupling scale visible in structure growth (S8) with opposite sign to w0wa",
                "a compact-dimension length that is independently constrained by tower of Kaluza-Klein modes",
            ],
            mimicable_by_existing_dof=0.72,  # w0wa already absorbs DESI evolving-w preference
            independent_probes=1,  # DESI DR2 is the original residual, not independent
            unique_probe_hits=0,  # Rubin/Euclid/Roman not yet the unique test
            pipeline_still_lcdm=True,
        ),
        patch_is_successor_or_mimic(
            name="Early dark energy as H0 patch",
            unique_predictions=[
                "CMB high-ell residuals distinct from Neff",
                "does not worsen S8",
            ],
            mimicable_by_existing_dof=0.85,
            independent_probes=2,
            unique_probe_hits=0,
            pipeline_still_lcdm=True,
        ),
        patch_is_successor_or_mimic(
            name="Pop III mixed-mass candidate threshold (>25% metal-free)",
            unique_predictions=[
                "zero-metal He II clump with no AGN mimic and no associated metal lines",
            ],
            mimicable_by_existing_dof=0.6,
            independent_probes=0,
            unique_probe_hits=0,
            pipeline_still_lcdm=True,
        ),
        patch_is_successor_or_mimic(
            name="Bottom-heavy IMF as JWST-mass patch",
            unique_predictions=[
                "direct spectroscopic dwarf-star signatures at z~0.7 descendants",
            ],
            mimicable_by_existing_dof=0.35,
            independent_probes=1,
            unique_probe_hits=1,  # Nature Astronomy 2026 measured it at z≈0.7
            pipeline_still_lcdm=True,
        ),
    ]

    novelty_cap = 0.44  # capped: extra-dimension and EDE patches have prior art; class is the move
    coherence = 0.73

    winning = gaps[0] if gaps else (penalized[0] if penalized else rows[0])

    out = {
        "session_id": "2026-09-08-ppc-patch-proliferation",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "winning_class": "Patch-Proliferation Class (PPC)",
        "iterate_class": "Exported-Prior Class (EPC)",
        "iterate2_class": "Successor-vs-Mimic gate",
        "novelty_cap": novelty_cap,
        "coherence": coherence,
        "counts": {
            "STRUCTURAL_GAP": len(gaps),
            "PENALIZED": len(penalized),
            "KILLED_OR_ZEROED": len(killed),
        },
        "primary": winning,
        "gaps": gaps,
        "penalized": penalized,
        "killed": killed,
        "all_ppc": rows,
        "epc_iterate": epc,
        "mimic_gate": mimic_tests,
        "prior_classes_subtracted": len(PRIOR_CLASSES),
        "zero_controls": ZERO_CONTROLS,
        "hygiene": (
            "Scores are a classification heuristic, not measurements of nature. "
            "Nothing here is a new particle, a new organism, or a proved mechanism. "
            "Copyright may protect this expression. It does not confer scientific "
            "priority, patent rights, or validation of any natural hypothesis."
        ),
    }
    return out


def render_text(out: dict) -> str:
    lines = [
        f"WINNING CLASS: {out['winning_class']}",
        f"novelty_cap {out['novelty_cap']} | coherence {out['coherence']}",
        f"STRUCTURAL_GAP {out['counts']['STRUCTURAL_GAP']} | PENALIZED {out['counts']['PENALIZED']} | KILLED/ZEROED {out['counts']['KILLED_OR_ZEROED']}",
        f"primary {out['primary']['id']} {out['primary']['score']}",
        "",
        "PPC RANKED",
        "----------",
    ]
    for r in out["all_ppc"]:
        lines.append(f"  {r['score']:6.2f}  {r['status']:16s}  {r['id']:22s}  {r['realm']}")
    lines += ["", "EPC ITERATE", "-----------"]
    for r in out["epc_iterate"]:
        lines.append(f"  {r['score']:6.2f}  {r['status']:16s}  {r['name']}")
    lines += ["", "SUCCESSOR vs MIMIC", "------------------"]
    for r in out["mimic_gate"]:
        lines.append(f"  {r['verdict']:16s}  {r['name']}")
        lines.append(f"                   {r['why']}")
    return "\n".join(lines)


if __name__ == "__main__":
    result = run()
    out_dir = Path("/workspace/artifacts")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "ppc_engine_output.json").write_text(json.dumps(result, indent=2))
    text = render_text(result)
    (out_dir / "ppc_engine_output.txt").write_text(text)
    print(text)
    print("\nJSON written to /workspace/artifacts/ppc_engine_output.json")
