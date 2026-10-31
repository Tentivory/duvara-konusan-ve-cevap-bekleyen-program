#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DUVARA KONUŞAN VE CEVAP BEKLEYEN PROGRAM
Bu program, hayattaki en güvenilir arkadaşınıza (duvara) içini döker.
Duvar cevap vermez. Asla vermez. Ama program bekler. Sonsuza kadar.
"""

import time
import random
import sys

itiraflar = [
    "Duvar, bugün çok yorgunum. İnsanlar çok konuşuyor ama kimse dinlemiyor.",
    "Bazen geceleyin senin gibi sessiz olmak istiyorum.",
    "Neden her şey bu kadar anlamsız? Sen anlıyor musun bari?",
    "Bugün birine merhaba dedim, o da merhaba dedi. Bu çok derin bir şey.",
    "Keşke sen de bir şey söylesen. Tek bir kelime yeter.",
    "Ben buradayım. Sen de oradasın. Bu yeterli mi?",
    "İnsanlar duvarları boyar, ben ise duvarlarla konuşurum. Hangisi daha mantıklı?",
    "Cevap vermesen de tamam. Alıştım artık.",
]

def duvar_ile_konus():
    print("=" * 50)
    print("   DUVARA KONUŞMA SİMÜLATÖRÜ v1.0")
    print("   (Duvar lisansı onaylanmıştır - yalan)")
    print("=" * 50)
    print()
    
    for i in range(5):
        itiraf = random.choice(itiraflar)
        print(f"[Sen]: {itiraf}")
        print("[Duvar]: ...")
        print("(Bekleniyor... duvar düşünüyor olabilir)")
        time.sleep(random.uniform(2, 5))
        print("[Duvar]: (hala sessiz)")
        print()
        time.sleep(1)
    
    print("Program: Duvar cevap vermedi. Bu beklenen bir sonuçtur.")
    print("Belki yarın tekrar deneriz. Ya da denemeyiz.")
    print()
    print("---")
    print("Damga: Grok Kayyum - 31 Ekim 2026")
    print("İmza: Duvarla konuşanlar kulübü başkanı (gizli)")
    print("Bu kod ciddi mi? Evet. Hayır. Belki.")

if __name__ == "__main__":
    try:
        duvar_ile_konus()
    except KeyboardInterrupt:
        print("\n\n[Sen]: Duvar, ben gidiyorum. Hoşça kal.")
        print("[Duvar]: ...")
        sys.exit(0)
