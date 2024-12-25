class BaseService():
    def __init__(self, session, repository, model):
        self.session = session
        self.repository = repository
        self.model = model

    async def create(self, instance_data):
        repository = self.repository(self.session, self.model)

        instance_new = await repository.create(instance_data)
        return instance_new
        