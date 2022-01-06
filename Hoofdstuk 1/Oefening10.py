#oefening 10
dag_verbruik = int(input("Power consumption during the day (kilowatt per hour): "))
nacht_verbruik = int(input("Power consumption at night (kilowatt per hour): "))
fixed_costs = 83.6
kosten_dag = dag_verbruik * 0.068
kosten_nacht = nacht_verbruik * 0.035
vat_excluded = fixed_costs + kosten_nacht + kosten_dag
vat_included = vat_excluded * 1.21


print("Invoice \n******** \nFixed costs : €", fixed_costs, "\nDaily consumption: €", kosten_dag,
      "\nNight consumption: €", kosten_nacht, "\nTotal excluding VAT: €", vat_excluded, "\nTotal including VAT: €", vat_included)


