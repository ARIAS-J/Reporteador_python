import json
import os

from pyreportjasper import PyReportJasper

from utils.constants import SalarioBase, Motivos


def generar_reporte(body):
    try:
        print("body.salario:", body.salario)
        print("SalarioBase.SALARIO:", SalarioBase.SALARIO)

        data_report = {
            'nombre_field': body.nombre,
            'apellido_field': body.apellido,
            'ocupacion_field': body.ocupacion,
            'salario': body.salario
        }

        if body.salario < SalarioBase.SALARIO:
            input_file = './template/reporte_contrato_rechazo.jrxml'
            data_report['motivo_rechazo'] = Motivos.SALARIO_INSUFICIENTE
        else:
            input_file = './template/reporte_contrato_afiliacion.jrxml'

        data = json.dumps(data_report)

        with open('data_report.json', 'w', encoding='utf-8') as file:
            file.write(data)

        out_file = './reporte_generado/reporte_python'
        conn = {
            'driver': 'json',
            'data_file': 'data_report.json',
        }

        pyreport_jasper = PyReportJasper()

        pyreport_jasper.config(
            input_file=input_file,
            output_file=out_file,
            output_formats=['pdf'],
            db_connection=conn
        )

        # Generar el reporte
        pyreport_jasper.process_report()

        # Devolver el path y el basename del documento  para descargar el PDF generado
        report_path = out_file
        report_filename = os.path.basename(out_file)

        data = {
            'report_path': report_path,
            'report_filename': report_filename
        }

        return data

    except Exception as e:
        print(f"An error occurred: {e}")
        return e
