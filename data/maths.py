rate=0.16; w_load=450; w_idle=90; h_load=8
kwh_load  = w_load*h_load*365/1000
kwh_idle  = w_idle*(24-h_load)*365/1000
kwh_247   = w_load*24*365/1000
print(f"load 8h/day      : {kwh_load:7.0f} kWh  -> ${kwh_load*rate:7.2f}")
print(f"+ idle 16h       : {kwh_load+kwh_idle:7.0f} kWh  -> ${(kwh_load+kwh_idle)*rate:7.2f}")
print(f"24/7 at full load: {kwh_247:7.0f} kWh  -> ${kwh_247*rate:7.2f}")
print(f"\nmy script claimed $210 / $412 / $631")
print(f"correct          ${kwh_load*rate:.0f} / ${(kwh_load+kwh_idle)*rate:.0f} / ${kwh_247*rate:.0f}")
print(f"$412 would need  {(412/rate):.0f} kWh = {412/rate/w_load:.1f} h/day at 450 W")
