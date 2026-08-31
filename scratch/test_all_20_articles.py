import urllib.request
import re

slugs = [
    "harmonizacao-facial-mitos-e-verdades-curitiba",
    "harmonizacao-facial-masculina-guia-curitiba",
    "botox-preventivo-quando-comecar-curitiba",
    "quanto-tempo-dura-o-botox-curitiba",
    "fios-de-pdo-lifting-sem-cirurgia-curitiba",
    "fios-de-pdo-ou-bioestimulador-qual-escolher",
    "sculptra-radiesse-elleva-comparativo-curitiba",
    "como-tratar-flacidez-facial-pescoco-curitiba",
    "preenchimento-labial-natural-lips-curitiba",
    "cuidados-pos-preenchimento-labial-guia",
    "rinomodelacao-com-acido-hialuronico-curitiba",
    "rinomodelacao-doi-cuidados-e-duracao",
    "estetica-intima-preenchimento-acido-hialuronico-curitiba",
    "rejuvenescimento-intimo-beneficios-e-autoestima",
    "protocolo-bioforce-regeneracao-celular-curitiba",
    "peptideos-bioativos-e-antiaging-avancado",
    "ozonioterapia-beneficios-estetica-saude-curitiba",
    "ozonioterapia-para-rejuvenescimento-e-cicatrizacao",
    "terapia-capilar-para-queda-de-cabelo-curitiba",
    "microinfusao-capilar-e-fortalecimento-dos-fios"
]

print(f"Total articles to audit: {len(slugs)}")
for i, s in enumerate(slugs, 1):
    url = f"http://localhost:8055/{s}"
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    # Find all images
    imgs = re.findall(r'<img[^>]+src="([^">]+)"', html)
    print(f"[{i:02d}/20] {s}: Status {req.status} | Imgs: {len(imgs)} | {imgs[:2]}")

