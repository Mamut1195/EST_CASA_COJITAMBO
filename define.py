import os
import sys
import comtypes.client


#set the following flag to True to attach to an existing instance of the program
#otherwise a new instance of the program will be started
AttachToInstance = True

#set the following flag to True to manually specify the path to ETABS.exe
#this allows for a connection to a version of ETABS other than the latest installation
#otherwise the latest installed version of ETABS will be launched
SpecifyPath = False

#if the above flag is set to True, specify the path to ETABS below
ProgramPath = r"C:\Program Files\Computers and Structures\ETABS 19\ETABS.exe"

#full path to the model
#set it to the desired path of your model
APIPath = r'C:\Users\joftv\OneDrive\Documentos\MAMPRO\CSI API'
if not os.path.exists(APIPath):
    try:
        os.makedirs(APIPath)
    except OSError:
        pass
ModelPath = APIPath + os.sep + 'API_1-001.edb'

#create API helper object
helper = comtypes.client.CreateObject('ETABSv1.Helper')
helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)

if AttachToInstance:
    #attach to a running instance of ETABS
    try:
        #get the active ETABS object
        myETABSObject = helper.GetObject("CSI.ETABS.API.ETABSObject") 
    except (OSError, comtypes.COMError):
        print("No running instance of the program found or failed to attach.")
        sys.exit(-1)
else:
    if SpecifyPath:
        try:
            #'create an instance of the ETABS object from the specified path
            myETABSObject = helper.CreateObject(ProgramPath)
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program from " + ProgramPath)
            sys.exit(-1)
    else:
        try: 
            #create an instance of the ETABS object from the latest installed ETABS
            myETABSObject = helper.CreateObjectProgID("CSI.ETABS.API.ETABSObject") 
        except (OSError, comtypes.COMError):
            print("Cannot start a new instance of the program.")
            sys.exit(-1)

    #start ETABS application
    myETABSObject.ApplicationStart()

#create SapModel object
SapModel = myETABSObject.SapModel
class MateriaProps:
    def __init__(self) -> None:
        pass

    def CrearConcreto(self, name:str, fc:float, IsLightweight:bool = False, FcsFactor:float = 1, SSType:int = 1,
                      SSHysType:int = 0, StrainAtFc:float = 0.0022, StrainUltimate:float = 0.0052, FrictionAngle:float =0,
                       DilatationalAngle:float = 0, Temp:float = 0 ):
        #Definir unidades kgf_cm
        SapModel.SetPresentUnits(14)

        print('Ingrese los valores en kgf_cm')
        
        # 2 = Concreto
        SapModel.PropMaterial.SetMaterial(name, 2)

        return (SapModel.PropMaterial.SetOConcrete(name, fc, IsLightweight, FcsFactor, SSType, SSHysType, StrainAtFc,
                                                    StrainUltimate, FrictionAngle, DilatationalAngle, Temp ))
    
    def CrearAceroA36(self, name:str = 'ASTM_A36'):
        
        #Definir unidades kgf_cm
        SapModel.SetPresentUnits(14)
        
        #1 = Acero
        SapModel.PropMaterial.SetMaterial(name, 1)

        SapModel.PropMaterial.SetOSteel(name, 2531.05, 4077.8, 3796.58, 4485.58, 1, 0, 0.02, 
                                        0.14, 0.2, 0 )
        
    def CrearAceroA53(self, name:str = 'ASTM_A53'):

        #Definir unidades kgf_cm
        SapModel.SetPresentUnits(14)
        
        #1 = Acero
        SapModel.PropMaterial.SetMaterial(name, 1)

        SapModel.PropMaterial.SetOSteel(name, 2460.74, 4218.42, 2706.82, 4640.26, 1, 0, 0.02, 
                                        0.14, 0.2, 0 )



class SectionProps:
    def __init__(self) -> None:
        pass

    def SeccionTubo(self, name:str, matprop:str, t3:int, t2:int, tf:int, tw:int,  ):
        SapModel.PropFrame.SetTube(name, matprop, t3, t2, tf, tw)
        #Definir unidades kgf_cm
        SapModel.SetPresentUnits(14)

        print('Ingrese los valores en kgf_cm')

class MassSourceNEC15:
    def __init__(self) ->None:
        pass
    
    def CasoGeneral(self, opcion:int=3, loads:int = 2, loadpat:list = ['Muerta', 'Viva'], SF:list = [1,0.25]):
        return (SapModel.PropMaterail.SetMassSource(opcion, loads, loadpat, SF))
    
    def CasoAlmacenaje(self, opcion:int=3, loads:int = 2, loadpat:list = ['Muerta', 'Viva'], SF:list = [1,0.5]):
        return (SapModel.PropMaterail.SetMassSource(opcion, loads, loadpat, SF))
    
class LoadPatternsNEC15:
    def __init__(self) -> None:
        print('Solo añade las cargas a la interfaz, \
              cargas sismas se añaden y se configuran desde la interfaz')

    def CargaMuerta(self):
        return(SapModel.LoadPatterns.SetLoadType('Muerta',1))
    
    def CargaViva(self):
        return(SapModel.LoadPatterns.SetLoadType('Viva',3))
    
    def CargaVivaCubierta(self):
        return(SapModel.LoadPatterns.SetLoadType('Viva Cubierta',3))
    
    def CargaGranizo(self):
        return(SapModel.LoadPatterns.SetLoadType('Granizo',7))
    
    def CargaViento(self):
        return(SapModel.LoadPatterns.SetLoadType('Viento',6))
    
class LoadCasesNEC15:
    

class LoadCombinacionesNEC15:
    def __init__(self, Carga_viva:int, Carga_muerta:int, Carga_viva_cubierta:int, Carga_de_granizo:int, Carga_de_viento:int ):
        self.Carga_viva = Carga_viva
        self.Carga_Muerta = Carga_muerta
        self.Carga_viva_cubierta = Carga_viva_cubierta
        self.Carga_de_granizo = Carga_de_granizo
        self.Carga_de_viento = Carga_de_viento

    def Combinacion1Nec(self, name:str = 'Combinación 1' ):
        SapModel.RespCombo.Add(name, 0)

        return(SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 1.4))

    def Combinacion2Nec(self, name:str = 'Combinación 2'):
  
        if self.Carga_viva_cubierta > self.Carga_de_granizo:
            return (SapModel.RespCombo.SetCaseList(name, 0, 'Viva Cubierta', 0, 0.5),SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 1.2),
                    SapModel.RespCombo.SetCaseList(name, 0, 'Viva', 0, 1.6))
        else :
            return(SapModel.RespCombo.SetCaseList(name, 0, 'Granizo', 0, 0.5),
                   SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 1.2),
                    SapModel.RespCombo.SetCaseList(name, 0, 'Viva', 0, 1.6))
  
    def Combinacion3Nec(self, name:str = 'Combinación 3'):
        if self.Carga_viva_cubierta > self.Carga_de_granizo:
            b = SapModel.RespCombo.SetCaseList(name, 0, 'Viva Cubierta', 0, 1.6)
        else :
            b = SapModel.RespCombo.SetCaseList(name, 0, 'Granizo', 0, 1.6)

        if self.Carga_viva > 0.5 * self.Carga_de_viento:
            c = SapModel.RespCombo.SetCaseList(name, 0, 'Viva', 0, 1)
        else:
            c = SapModel.RespCombo.SetCaseList(name, 0, 'Viento', 0, 0.5)

        return(SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 1.2),b,c)

    def Combinacion4Nec(self, name:str = 'Combinación 4'):
        a = SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 1.2)

        b = SapModel.RespCombo.SetCaseList(name, 0, 'Viento', 0, 1)

        c = SapModel.RespCombo.SetCaseList(name, 0, 'Viva', 0, 1)

        if self.Carga_viva_cubierta > self.Carga_de_granizo:
            d = SapModel.RespCombo.SetCaseList(name, 0, 'Viva Cubierta', 0, 0.5)
        else:
            d = SapModel.RespCombo.SetCaseList(name, 0, 'Granizo', 0, 0.5)

        return(a,b,c,d)

    def Combinacion5Nec(self, name:str = 'Combinación 5'):
        a = SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 1.2)

        c = SapModel.RespCombo.SetCaseList(name, 0, 'Viva', 0, 1)

        d = SapModel.RespCombo.SetCaseList(name, 0, 'Viento', 0, 0.2)

        print('Añadir desde la interfaz el simo a esta combinacion')

        return(a,c,d)
    
    def Combinacion6Nec(self, name:str = 'Combinación 6'):
        a = SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 0.9)

        b = SapModel.RespCombo.SetCaseList(name, 0, 'Viento', 0, 1)

        return(a,b)

    def Combinacion7Nec(self, name:str = 'Combinación 7'):
        a = SapModel.RespCombo.SetCaseList(name, 0, 'Muerta', 0, 0.9)

        print('Añadir desde la interfaz el simo a esta combinacion')
      
        return(a)

    

    

