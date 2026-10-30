# -*- coding: utf-8 -*-
"""
Run FUSION build for BYTE-CONTEXT (Episode 13)
Synthesizes speech, generates word boundaries, builds self-contained HTML,
copies canonical deliverables to episodes/, and produces SHA-256 manifest.
"""
import os
import sys
import shutil
import hashlib
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT, "data")
EPISODES_DIR = os.path.join(ROOT, "episodes")
CHAD_DIR = r"c:\Users\jibra\Desktop\1\Chad_Visuals"

sys.path.insert(0, DATA_DIR)
os.environ["FUSION_SPEC"] = "spec_context"

import fusion_build

print("=" * 70)
print("STARTING AUTONOMOUS FUSION BUILD FOR BYTE-CONTEXT")
print("=" * 70)

out = fusion_build.build()
print("\nBuild returned HTML path:", out)

NAME = "BYTE-CONTEXT"
deliverables = [".html", ".srt", "-scenes.txt", "-chapters.txt"]

print("\n--- Synchronizing Canonical Deliverables to episodes/ & Chad_Visuals ---")
for ext in deliverables:
    src = os.path.join(ROOT, NAME + ext)
    dst_epis = os.path.join(EPISODES_DIR, NAME + ext)
    dst_chad = os.path.join(CHAD_DIR, NAME + ext)
    
    assert os.path.exists(src), f"Missing built deliverable: {src}"
    
    shutil.copy2(src, dst_epis)
    print(f"  Copied {src} -> {dst_epis}")
    
    if os.path.exists(CHAD_DIR):
        shutil.copy2(src, dst_chad)
        print(f"  Copied {src} -> {dst_chad}")

# Verify 100% bitwise identity between root and episodes
h_root = hashlib.sha256(open(os.path.join(ROOT, NAME + ".html"), "rb").read()).hexdigest()
h_epis = hashlib.sha256(open(os.path.join(EPISODES_DIR, NAME + ".html"), "rb").read()).hexdigest()
assert h_root == h_epis, f"CANONICAL DIVERGENCE: root ({h_root}) != episodes ({h_epis})"
print(f"\n✅ CANONICAL SOURCE IDENTITY VERIFIED: {h_root}")

# Generate Authoritative SHA-256 Release Manifest
manifest = {
    "episode": NAME,
    "title": "128K CONTEXT WINDOW: THE SILENT MEMORY TRAP",
    "artifacts": {}
}

for ext in deliverables:
    p = os.path.join(EPISODES_DIR, NAME + ext)
    manifest["artifacts"][f"episodes/{NAME}{ext}"] = hashlib.sha256(open(p, "rb").read()).hexdigest()

manifest_path = os.path.join(EPISODES_DIR, f"{NAME}-manifest.json")
with open(manifest_path, "w", encoding="utf-8") as mf:
    json.dump(manifest, mf, indent=2)

print(f"✅ Generated Authoritative Manifest: {manifest_path}")
print("=" * 70)
print("BYTE-CONTEXT BUILD & PACKAGING COMPLETE!")
print("=" * 70)
