from engine.subaction import *

class debugAction(SubAction):
    fields = [NodeMap('statement','string','print','')
              ]
    
    def __init__(self,_statement=''):
        SubAction.__init__(self)
        self.statement = _statement
        
    def execute(self, _action, _actor):
        SubAction.execute(self, _action, _actor)
        if isinstance(self.statement, tuple):
            source,name = self.statement
            if source == 'action':
                print('action.'+name+': '+str(getattr(_action, name)))
            else:
                if hasattr(_actor, 'stats') and _actor.stats.has_key(name):
                    print('object['+name+']: '+str(_actor.stats[name]))
                else:
                    print('object.'+name+': '+str(getattr(_actor, name)))
        else:
            print(self.statement)
    
    def getDisplayName(self):
        return 'Print Debug'
