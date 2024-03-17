import os

from fastapi import APIRouter, Response, HTTPException

from models.models import ContratoAfiliacion
from reporteador.app import generar_reporte

router = APIRouter()


@router.post('/generar_reporte')
def generar_reporte_py(body: ContratoAfiliacion):

    print(body)
    data = generar_reporte(body=body)

    report_path = data['report_path']
    report_filename = data['report_filename']

    if os.path.exists(report_path + '.pdf'):
        # Devolver el archivo de reporte para descargar
        return Response(content=open(report_path + '.pdf', 'rb').read(), media_type='application/pdf',
                        headers={"Content-Disposition": f"attachment; filename={report_filename}.pdf"})
    else:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
