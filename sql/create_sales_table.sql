CREATE TABLE public.sales (
	"date" date NULL,
	shop_num int NULL,
	cash_num int NULL,
	doc_id numeric NULL,
	item varchar NULL,
	category varchar NULL,
	amount int NULL,
	price float4 NULL,
	discount int NULL,
	CONSTRAINT sales_unique UNIQUE (doc_id,item)
);
COMMENT ON TABLE public.sales IS 'Contatins data from cash registers from all shops';
