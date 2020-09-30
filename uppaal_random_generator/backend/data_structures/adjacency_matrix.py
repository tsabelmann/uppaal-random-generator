# Import A
import abc


class AbstractAdjacencyMatrix(abc.ABC):
    @abc.abstractmethod
    def has_edge_from_to(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def set_edge_from_to(self, v1, v2):
        pass
    
    @abc.abstractmethod
    def remove_edge_from_to(self, v1, v2):
        pass

    @abc.abstractmethod
    def d_out(self, v):
        pass

    @abc.abstractmethod
    def d_in(self, v):
        pass


class SimpleAdjacencyMatrix(AbstractAdjacencyMatrix):
    def __init__(self, N, default_value=0):
        # Adjacency Matrix Dimension
        self._N = N
        # Adjacency Matrix Data
        self._edge_data = [[default_value for _ in range(N)] for _ in range(N)]
        # Degree Matrix
        self._degree_data = [[0, 0] for _ in range(N)] if not default_value else [[N, N] for _ in range(N)]

    @property
    def N(self):
        return self._N

    @property
    def edge_data(self):
        return self._edge_data

    @property
    def degree_data(self):
        return self._degree_data

    def has_edge_from_to(self, v1, v2):
        if self._edge_data[v1][v2]:
            return True
        else:
            return False
    
    def set_edge_from_to(self, v1, v2):
        if self.has_edge_from_to(v1, v2):
            print(f'WARNING: Set Edge from {v1} to {v2} that was already set')
        else:
            # Set Edge between vertex v1 and v2
            self.edge_data[v1][v2] = 1
            # Increment Output Degree of vertex v1
            self.degree_data[v1][0] += 1
            # Increment Input Degree of vertex v2
            self.degree_data[v2][1] += 1

    def remove_edge_from_to(self, v1, v2):
        if self.has_edge_from_to(v1, v2):
            # Remove Edge between vertex v1 and v2
            self.edge_data[v1][v2] = 0
            # Decrement Output Degree of vertex v1
            self.degree_data[v1][0] -= 1
            # Decrement Input Degree of vertex v2
            self.degree_data[v2][1] -= 1
        else:
            print(f'WARNING: Removed Edge from {v1} to {v2} that was already removed')

    def d_out(self, v):
        if 0 <= v < self.N:
            return self.degree_data[v][0]
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')

    def d_in(self, v):
        if 0 <= v < self.N:
            return self.degree_data[v][1]
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')

    def d_in_min(self):
        return min((self.degree_data[v][1] for v in range(self.N)))
    
    def d_in_max(self):
        return max((self.degree_data[v][1] for v in range(self.N)))

    def d_out_min(self):
        return min((self.degree_data[v][0] for v in range(self.N)))

    def d_out_max(self):
        return max((self.degree_data[v][0] for v in range(self.N)))

    def get_edges(self):
        return [(v1, v2) for v1 in range(self.N) for v2 in range(self.N) if self.edge_data[v1][v2]]

    def get_incoming_edges_from_end(self, v):
        if 0 <= v <= self.N:
            return [(v1, v) for v1 in range(self.N) if self.edge_data[v1][v]]
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')
    
    def get_outgoing_edges_from_start(self, v):
        if 0 <= v <= self.N:
            return [(v, v2) for v2 in range(self.N) if self.edge_data[v][v2]]
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')
    
    def get_end_points_from_start(self, v):
        if 0 <= v < self.N:
            lst = []
            for v2 in range(self.N):
                if self.has_edge_from_to(v, v2):
                    lst.append(v2) 

            return lst
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')

    def get_starting_points_from_end(self, v):
        if 0 <= v < self.N:
            lst = []
            for v1 in range(self.N):
                if self.has_edge_from_to(v1, v):
                    lst.append(v1)
            return lst
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')


class AdvancedAdjacencyMatrix(AbstractAdjacencyMatrix):
    def __init__(self, N, default_value=0):
        # Adjacency Matrix Dimension
        self._N = N
        # Adjacency Matrix Data
        self._edge_data = {i: {j: default_value for j in range(N)} for i in range(N)}
        # Degree Matrix
        self._degree_data = {i: dict(d_in=N*default_value, d_out=N*default_value) for i in range(N)}

    @property
    def N(self):
        return self._N

    @property
    def edge_data(self):
        return self._edge_data

    @property
    def degree_data(self):
        return self._degree_data

    def has_edge_from_to(self, v1, v2):
        if self.edge_data[v1][v2]:
            return True
        else:
            return False

    def edges_from_to(self, v1, v2):
        return self.edge_data[v1][v2]

    def set_edge_from_to(self, v1, v2):
        # Add Edge from v1 to v2
        self.edge_data[v1][v2] += 1
        # Update Output Degree of v1
        self.degree_data[v1]['d_out'] += 1
        # Update Input Degree of v2
        self.degree_data[v2]['d_in'] += 1
    
    def remove_edge_from_to(self, v1, v2):
        if self.edge_data[v1][v2]:
            # Remove Edge from v1 to v2
            self.edge_data[v1][v2] -= 1
            # Update Output Degree of v1
            self.degree_data[v1]['d_out'] -= 1
            # Update Input Degree of v2
            self.degree_data[v2]['d_in'] -= 1
        else:
            print(f'WARNING: No Edge from {v1} to {v2}...')

    def d_out(self, v):
        return self.degree_data[v]['d_out']

    def d_in(self, v):
        return self.degree_data[v]['d_in']

    def d_in_min(self):
        return min((self.degree_data[v]['d_in'] for v in range(self.N)))
    
    def d_in_max(self):
        return max((self.degree_data[v]['d_in'] for v in range(self.N)))

    def d_out_min(self):
        return min((self.degree_data[v]['d_out'] for v in range(self.N)))

    def d_out_max(self):
        return max((self.degree_data[v]['d_out'] for v in range(self.N)))

    def get_edges(self):
        return [(v1, v2) for v1 in range(self.N) for v2 in range(self.N) for _ in range(self.edge_data[v1][v2])]

    def get_incoming_edges_from_end(self, v):
        if 0 <= v <= self.N:
            return [(v1, v) for v1 in range(self.N) for _ in range(self.edge_data[v1, v])]
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')
    
    def get_outgoing_edges_from_start(self, v):
        if 0 <= v <= self.N:
            return [(v, v2) for v2 in range(self.N) for _ in range(self.edge_data[v, v2])]
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')
    
    def get_end_points_from_start(self, v):
        if 0 <= v < self.N:
            lst = []
            for v2 in range(self.N):
                if self.has_edge_from_to(v, v2):
                    lst.append(v2) 

            return lst
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')

    def get_starting_points_from_end(self, v):
        if 0 <= v < self.N:
            lst = []
            for v1 in range(self.N):
                if self.has_edge_from_to(v1, v):
                    lst.append(v1)
            return lst
        else:
            raise IndexError('vertex index has to be in in the discrete interval [0, N)')
