#INFO: get dolar prices from Ambito

import requests
from time import time

URLs={
	'ccl': 'https://mercados.ambito.com//dolarrava/cl/variacion',
	'blue': 'https://mercados.ambito.com//dolar/informal/variacion',
}

CACHE_SECONDS= 60*10 #A: ten minutes

dontQueryBefore= 0 #U: cache values
PriceAsJsonLast= None

def priceAsJson():
	global PriceAsJsonLast, dontQueryBefore
	tNow= time()
	if PriceAsJsonLast is None or dontQueryBefore< tNow:
		try:
			r= {};
			for (k,url) in URLs.items():
				res= requests.get(url)
				r[k]= res.json()
				#ej. {'compra': '1164,60', 'venta': '1164,60', 'fecha': '15/01/2024 - 17:55', 'ultimo': '1136,65', 'valor': '1164,60', 'variacion': '2,50%', 'valor_cierre_ant': '1136,65', 'class-variacion': 'up'}
		
			PriceAsJsonLast= r;
			dontQueryBefore= tNow + CACHE_SECONDS
		except:
			pass
	
	return PriceAsJsonLast;

def priceAsText():
	return '\n'.join( [ f"{k}: {v['compra']} / {v['venta']} @ {v['fecha']}" for (k,v) in priceAsJson().items() ] )

