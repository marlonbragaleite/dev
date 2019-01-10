program FareController;
{$I+}

uses crt, sysutils;

const
     FileCliente = 'fare_cliente.fcontr';
     FileHistorico = 'fare_historico.fcontr';
     FileStatusLocacao = 'fare_status.fcontr';

type
     TCliente = record
        id:byte;
        nome:string[20];
     end;

     THistorico = record
        cliente: byte;
        checkin: TTimestamp;
        checkout: TTimestamp;
        minutos: integer;
     end;

     TStatusLocacao = record
        alugada: boolean;
        cliente: TCliente;
     end;

var
     Arq_Cliente: file of TCliente;
     Arq_Historico: file of THistorico;
     Arq_StatusLocacao: file of TStatusLocacao;

procedure IniciaArquivos();
begin
        AssignFile(Arq_Cliente, FileCliente);
        AssignFile(Arq_Historico, FileHistorico);
        AssignFile(Arq_StatusLocacao, FileStatusLocacao);
        try
                reset(Arq_Cliente);
                reset(Arq_Historico);
                reset(Arq_StatusLocacao);
        except
                rewrite(Arq_Cliente);
                rewrite(Arq_Historico);
                rewrite(Arq_StatusLocacao);
        end;
end;

procedure FechaArquivos();
begin
        try
                CloseFile(Arq_Cliente);
                CloseFile(Arq_Historico);
                CloseFile(Arq_StatusLocacao);
        except
        end;
end;

function status_locacao():integer;
begin

end;

begin
        IniciaArquivos;


        FechaArquivos;


end.