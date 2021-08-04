from rolepermissions.roles import AbstractUserRole

class SystemManager(AbstractUserRole):
    available_permissions = {
        'drop_tables': True,
        'Can add user':True,
        'Can change user':True,
        'Can view user':True,
        'Can delete user':True,
        'Can delete task':True,
        'Can change task':True,
        'Can view task':True,
        
    }

class Doctor(AbstractUserRole):
    available_permissions = {
        'create_medical_record': True,
    }

class Nurse(AbstractUserRole):
    available_permissions = {
        'edit_patient_file': True,
    }
    