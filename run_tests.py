"""
Script para ejecutar los tests de Reciclapp
Facilita la ejecución de tests con diferentes configuraciones
"""

import sys
import subprocess
import argparse


def run_command(command):
    """Ejecuta un comando y retorna el código de salida"""
    print(f"\n🔧 Ejecutando: {' '.join(command)}\n")
    result = subprocess.run(command, shell=True)
    return result.returncode


def main():
    """Función principal del script"""
    parser = argparse.ArgumentParser(description='Ejecutar tests de Reciclapp')
    parser.add_argument(
        '--mode',
        choices=['all', 'unit', 'integration', 'ui', 'coverage', 'quick'],
        default='all',
        help='Modo de ejecución de tests'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Modo verbose'
    )
    parser.add_argument(
        '--file',
        '-f',
        type=str,
        help='Archivo específico de tests a ejecutar'
    )
    
    args = parser.parse_args()
    
    # Comando base
    base_cmd = ['pytest']
    
    # Añadir verbose si se especifica
    if args.verbose:
        base_cmd.append('-vv')
    
    # Configurar según el modo
    if args.mode == 'all':
        print("🧪 Ejecutando TODOS los tests...")
        cmd = base_cmd
    
    elif args.mode == 'unit':
        print("🔬 Ejecutando tests UNITARIOS...")
        cmd = base_cmd + ['-m', 'unit']
    
    elif args.mode == 'integration':
        print("🔗 Ejecutando tests de INTEGRACIÓN...")
        cmd = base_cmd + ['-m', 'integration']
    
    elif args.mode == 'ui':
        print("🎨 Ejecutando tests de UI...")
        cmd = base_cmd + ['-m', 'ui']
    
    elif args.mode == 'coverage':
        print("📊 Ejecutando tests con COBERTURA...")
        cmd = base_cmd + [
            '--cov=app',
            '--cov-report=html',
            '--cov-report=term-missing',
            '--cov-branch'
        ]
    
    elif args.mode == 'quick':
        print("⚡ Ejecución RÁPIDA (sin cobertura)...")
        cmd = base_cmd + ['-x', '--tb=short']
    
    # Añadir archivo específico si se especifica
    if args.file:
        print(f"📄 Ejecutando tests de: {args.file}")
        cmd.append(args.file)
    
    # Ejecutar los tests
    exit_code = run_command(cmd)
    
    # Mensaje final
    if exit_code == 0:
        print("\n✅ ¡Todos los tests pasaron exitosamente!")
        
        if args.mode == 'coverage':
            print("\n📊 Reporte de cobertura generado en: htmlcov/index.html")
            print("   Ábrelo en tu navegador para ver los detalles.")
    else:
        print("\n❌ Algunos tests fallaron. Revisa los errores arriba.")
        sys.exit(exit_code)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrumpidos por el usuario")
        sys.exit(1)

