from django.core.exceptions import ValidationError

class ContainLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError('Le mot de passe doit contenir au moins une lettre', code='password_no_letter')
        
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'
    

class ContainNumberValidator:
    def validate(self, password, user=None):
        if not any(character.isdigit() for character in password):
            raise ValidationError('Le mot de passe doit contenir au moins un chiffre.', code='password_no_number')
        
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au mois un chiffre.'