default_path = "Find or Create a database." #you can set a default path so you dont find database everytime you run.
default_query = "Write you query here and click run." #this will be in the query text area.
connect_on_open = False #connect automatically usin the dafult_path when running the application.
table_name_on_col_dbl_click = False #insert table.column or just column when double clicking on tables tree view.

#Syntax highlight modefiy as you wish, one note though is that its a bit slow
syntax ={
    "keywords":{
        'style': {'foreground': '#0831e7'},
        'words': ['limit', 'and', 'or', 'as', 'case', 'between', 'by', 'case', 'cast', 'constraint', 'create', 'cross', 'cube', 'current_date', 'current_time', 'current_timestamp', 'current_user', 'deallocate', 'delete', 'describe', 'distinct', 'drop', 'else', 'end', 'escape', 'except', 'execute', 'exists', 'extract', 'false', 'for', 'from', 'full', 'group', 'grouping', 'having', 'in', 'inner', 'insert', 'intersect', 'into', 'is', 'join', 'left', 'like', 'localtime', 'localtimestamp', 'natural', 'normalize', 'not', 'null', 'on', 'or', 'order', 'outer', 'prepare', 'recursive', 'right', 'rollup', 'select', 'table', 'then', 'true', 'uescape', 'union', 'unnest', 'using', 'values', 'when', 'where', 'with']
        },
    "functions":{
        'style': {'foreground': '#e78708'},
        'words': ['all', 'any', 'attimezone', 'between', 'coalesce', 'current_date', 'current_time', 'current_timestamp', 'current_user', 'decimal', 'if', 'isdistinct', 'isnotdistinct', 'isnotnull', 'isnull', 'localtime', 'localtimestamp', 'not', 'notbetween', 'nullif', 'some', 'try', 'abs', 'acos', 'all_match', 'any_match', 'approx_distinct', 'approx_most_frequent', 'approx_percentile', 'approx_set', 'arbitrary', 'array_agg', 'array_distinct', 'array_except', 'array_intersect', 'array_join', 'array_max', 'array_min', 'array_position', 'array_remove', 'array_sort', 'array_union', 'arrays_overlap', 'asin', 'at_timezone', 'atan', 'atan2', 'avg', 'bar', 'beta_cdf', 'bing_tile_at', 'bing_tile_coordinates', 'bing_tile_polygon', 'bing_tile_zoom_level', 'bing_tile', 'bing_tiles_around', 'bit_count', 'bitwise_and_agg', 'bitwise_and', 'bitwise_not', 'bitwise_or_agg', 'bitwise_or', 'bitwise_xor', 'bool_and', 'bool_or', 'cardinality', 'cast', 'cbrt', 'ceil', 'ceiling', 'char2hexint', 'checksum', 'chr', 'classify', 'codepoint', 'color', 'combinations', 'concat', 'contains', 'convex_hull_agg', 'corr', 'cos', 'cosh', 'cosine_similarity', 'count_if', 'count', 'covar_pop', 'covar_samp', 'crc32', 'cume_dist', 'current_timezone', 'date_add', 'date_diff', 'date_format', 'date_parse', 'date_trunc', 'date', 'day_of_month', 'day_of_week', 'day_of_year', 'day', 'degrees', 'dense_rank', 'dow', 'doy', 'e', 'element_at', 'empty_approx_set', 'every', 'exp', 'extract', 'features', 'filter', 'first_value', 'flatten', 'floor', 'format', 'from_base', 'from_base64', 'from_base64url', 'from_big_endian_32', 'from_big_endian_64', 'from_encoded_polyline', 'from_hex', 'from_ieee754_32', 'from_ieee754_64', 'from_iso8601_date', 'from_iso8601_timestamp', 'from_unixtime', 'from_utf8', 'geometric_mean', 'geometry_from_hadoop_shape', 'geometry_invalid_reason', 'geometry_to_bing_tiles', 'geometry_union_agg', 'geometry_union', 'great_circle_distance', 'greatest', 'hamming_distance', 'histogram', 'hmac_md5', 'hmac_sha1', 'hmac_sha256', 'hmac_sha512', 'hour', 'index', 'infinity', 'inverse_beta_cdf', 'inverse_normal_cdf', 'is_finite', 'is_infinite', 'is_json_scalar', 'is_nan', 'json_array_contains', 'json_array_get', 'json_array_length', 'json_extract_scalar', 'json_extract', 'json_format', 'json_parse', 'json_size', 'kurtosis', 'lag', 'last_day_of_month', 'last_value', 'lead', 'learn_classifier', 'learn_libsvm_classifier', 'learn_libsvm_regressor', 'learn_regressor', 'least', 'length', 'levenshtein_distance', 'line_interpolate_point', 'line_interpolate_points', 'ln', 'log', 'log10', 'log2', 'lower', 'lpad', 'ltrim', 'map_agg', 'map_concat', 'map_entries', 'map_filter', 'map_from_entries', 'map_keys', 'map_values', 'map_zip_with', 'map', 'max_by', 'max', 'md5', 'merge', 'millisecond', 'min_by', 'min', 'minute', 'mod', 'month', 'multimap_agg', 'multimap_from_entries', 'nan', 'ngrams', 'none_match', 'normal_cdf', 'normalize', 'now', 'nth_value', 'ntile', 'numeric_histogram', 'parse_datetime', 'parse_duration', 'parse_presto_data_size', 'percent_rank', 'pi', 'position', 'pow', 'power', 'qdigest_agg', 'quarter', 'radians', 'rand', 'random', 'rank', 'reduce_agg', 'reduce', 'regexp_count', 'regexp_extract_all', 'regexp_extract', 'regexp_like', 'regexp_position', 'regexp_replace', 'regexp_split', 'regr_intercept', 'regr_slope', 'regress', 'render', 'repeat', 'replace', 'reverse', 'rgb', 'round', 'row_number', 'rpad', 'rtrim', 'second', 'sequence', 'sha1', 'sha256', 'sha512', 'shuffle', 'sign', 'simplify_geometry', 'sin', 'skewness', 'slice', 'split_part', 'split_to_map', 'split_to_multimap', 'split', 'spooky_hash_v2_32', 'spooky_hash_v2_64', 'sqrt', 'st_area', 'st_asbinary', 'st_astext', 'st_boundary', 'st_buffer', 'st_centroid', 'st_contains', 'st_convexhull', 'st_coorddim', 'st_crosses', 'st_difference', 'st_dimension', 'st_disjoint', 'st_distance', 'st_endpoint', 'st_envelope', 'st_envelopeaspts', 'st_equals', 'st_exteriorring', 'st_geometries', 'st_geometryfromtext', 'st_geometryn', 'st_geometrytype', 'st_geomfrombinary', 'st_interiorringn', 'st_interiorrings', 'st_intersection', 'st_intersects', 'st_isclosed', 'st_isempty', 'st_isring', 'st_issimple', 'st_isvalid', 'st_length', 'st_linefromtext', 'st_linestring', 'st_multipoint', 'st_numgeometries', 'st_numpoints', 'st_overlaps', 'st_point', 'st_pointn', 'st_points', 'st_polygon', 'st_relate', 'st_startpoint', 'st_symdifference', 'st_touches', 'st_union', 'st_within', 'st_x', 'st_xmax', 'st_xmin', 'st_y', 'st_ymax', 'st_ymin', 'starts_with', 'stddev_pop', 'stddev_samp', 'stddev', 'strpos', 'substr', 'substring', 'sum', 'tan', 'tanh', 'timezone_hour', 'timezone_minute', 'to_base', 'to_base64', 'to_big_endian_32', 'to_big_endian_64', 'to_char', 'to_date', 'to_encoded_polyline', 'to_geometry', 'to_hex', 'to_ieee754_32', 'to_ieee754_64', 'to_iso8601', 'to_milliseconds', 'to_spherical_geography', 'to_timestamp', 'to_unixtime', 'to_utf8', 'transform_keys', 'transform_values', 'transform', 'translate', 'trim', 'truncate', 'try_cast', 'typeof', 'upper', 'url_decode', 'url_encode', 'url_extract_fragment', 'url_extract_host', 'url_extract_parameter', 'url_extract_path', 'url_extract_port', 'url_extract_query', 'uuid', 'value_at_quantile', 'values_at_quantiles', 'var_pop', 'var_samp', 'variance', 'week_of_year', 'week', 'width_bucket', 'wilson_interval_lower', 'wilson_interval_upper', 'with_timezone', 'word_stem', 'xxhash64', 'year_of_week', 'year', 'yow', 'zip_with', 'zip']
        },
    "datatype":{
        'style': {'foreground': '#9e19d7'},
        'words': ['khyperloglog', 'boolean', 'tinyint', 'smallint', 'integer', 'bigint', 'real', 'double', 'decimal', 'varchar', 'char', 'varbinary', 'json', 'date', 'time', 'time with time zone', 'timestamp with time zone', 'interval year to month', 'interval day to second', 'timestamp', 'array', 'map', 'row', 'ipaddress', 'ipprefix', 'p4hyperloglog', 'qdigest']
        }    
    }

#where does a word end, helps in highlighting syntax
word_end = set([' ', '.', '"', "'", '{', '}', '[', ']', '(', ')', '=', '+', '-', '*', '/', '\\', '|', '<', '>', '%'])

import sqlite3 as sql
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import time
import pandas as pd

class sqllite3_gui:
    def __init__(self, master):
        self.root = master
        self.connected = False
        self.df = pd.DataFrame()
        
        #to call on_close when user exits the app
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        winW = int(self.root.winfo_screenwidth()/1.25)
        winH = int(self.root.winfo_screenheight()/1.25)
        
        self.root.title('SQLite3 Viewer')
        self.root.geometry(f'{winW}x{winH}+0+0')
        
        self.query_frame = tk.LabelFrame(self.root, text='Query')
        self.query_frame.place(relheight=.48, relwidth=.98, relx=.01)
        
        self.db_path = tk.StringVar()
        self.db_path.set(default_path)
        self.db_entry = tk.Entry(self.query_frame, text = self.db_path, font='helvetica 10', state='disabled')
        self.db_entry.place(relheight=.09, relwidth=.21, relx=.01)
        
        self.file_button = tk.Button(self.query_frame, text ="@", command=self.file_dialog, font='helvetica 10')
        self.file_button.place(relheight=.08, relwidth=.02, relx=.22)
        
        self.create_db_button = tk.Button(self.query_frame, text ="+", command=self.create_database, font='helvetica 10')
        self.create_db_button.place(relheight=.08, relwidth=.02, relx=.24)
        
        ## Treeview Widget. Ref: https://www.youtube.com/watch?v=PgLjwl6Br0k
        self.tables_tree = ttk.Treeview(self.query_frame)
        self.tables_tree.place(relwidth=.25, relheight=.90, relx=.01, rely=.09)
        self.tables_tree["show"] = "tree"
        self.tables_tree.bind("<Double-1>", self.OnDoubleClick)
        
        self.query_text = tk.Text(self.query_frame, font='helvetica 12')
        self.query_text.place(relwidth=.72, relheight=.90, relx=.27)
        self.query_text.bind("<Control-Return>", lambda e: self.run_query())
        
        #loops through the syntax dictionary to cread tags for each type
        for kw in syntax:
            self.query_text.tag_config(kw, **syntax[kw]['style'])
        
        self.query_text.insert('1.0', default_query)
        
        self.query_text.tag_configure("current_line", background="#e9e9e9")
        self.query_text.tag_add("current_line", "insert linestart", "insert lineend+1c")
        self.query_text.tag_raise("sel")
        
        self.query_text.bind("<KeyRelease>", lambda e: self.highlight())
        
        self.query_button = tk.Button(self.query_frame, text ="Run", command=self.run_query, font='helvetica 10')
        self.query_button.place(relheight=.08, relwidth=.05, relx=.27, rely=.91)
        
        self.result_frame = tk.LabelFrame(self.root, text='Result preview - Upto 1000 rows only, save to get the complete result.')
        self.result_frame.place(relheight=.48, relwidth=.98, rely=.48, relx=.01)
        
        ## Treeview Widget. Ref: https://www.youtube.com/watch?v=PgLjwl6Br0k
        self.result_treeview = ttk.Treeview(self.result_frame)
        self.result_treeview.place(relwidth=.98, relheight=.90, relx=.01, rely=0)
        
        self.treescrolly = tk.Scrollbar(self.result_treeview,
                                        orient="vertical",
                                        command=self.result_treeview.yview)
        
        self.treescrollx = tk.Scrollbar(self.result_treeview,
                                        orient="horizontal",
                                        command=self.result_treeview.xview)
        
        self.result_treeview.configure(xscrollcommand=self.treescrollx.set,
                                        yscrollcommand=self.treescrolly.set)
        
        self.treescrollx.pack(side="bottom", fill="x")
        self.treescrolly.pack(side="right", fill="y")

        self.save_button = tk.Button(self.result_frame, text ="Save", width=25, command=self.save_query, state=tk.DISABLED, font='helvetica 10')
        self.save_button.place(relheight=.09, relwidth=.05, relx=.01, rely=.90)
        
        self.clear_button = tk.Button(self.result_frame, text ="Clear", width=25, command=self.clear_output, state=tk.DISABLED, font='helvetica 10')
        self.clear_button.place(relheight=.09, relwidth=.05, relx=.07, rely=.90)
        
        self.status_frame = tk.Frame(self.root)
        self.status_frame.place(relheight=.4, relwidth=.98, relx=.01, rely=.96)
        
        self.status_title = tk.Label(self.status_frame, text = 'Status:', anchor='nw')
        self.status_title.place(relheight=1, relwidth=.05)
        
        
        self.status = tk.StringVar()
        self.status.set("Waiting for connection...")
        self.status_label = tk.Label(self.status_frame, textvariable = self.status, anchor='nw')
        self.status_label.place(relheight=1, relwidth=.95, relx=.05)
        
        if connect_on_open: self.connect()
        
        self.query_text.focus()
    
    # when click on '@' button, user is asked to select the db s/he wants to connect to
    def file_dialog(self):
        file = filedialog.askopenfile(defaultextension=".db", filetypes=(("SQLite3 Database", "*.db"),("All Files", "*.*") ))
        if file != None:
            self.db_path.set(file.name)
            self.db_entry.xview_moveto(1)
            self.connect()
    
    # when click on '+' button, user is asked to create a new db s/he and then the app connects to it
    def create_database(self):
       file = filedialog.asksaveasfile(defaultextension=".db", filetypes=(("SQLite3 Database", "*.db"),("All Files", "*.*") ))
       if file != None:
           self.db_path.set(file.name)
           self.db_entry.xview_moveto(1)
           self.connect()
    
    def connect(self):
        try:
            self.tables_tree.delete(*self.tables_tree.get_children())
            
            self.disconnect()
            
            self.conn = sql.connect(self.db_path.get())
            self.connected = True            
            
            self.update_tables_treeview()
            
            self.status.set("Conneted.")
            
        except Exception as e:
            self.status.set(f"Error connecting to Database: {str(e)}.")
    
    def update_tables_treeview(self):
        self.status.set("Reading database tables.")
        self.tables_tree.delete(*self.tables_tree.get_children())
        
        tblsDF = pd.read_sql("SELECT DISTINCT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'", self.conn)
        
        for tbl in sorted([t.lower() for t in list(tblsDF.name)]):
            cur = self.tables_tree.insert("", 'end', text=tbl)
            colsDF = pd.read_sql(f"PRAGMA table_info({tbl})", self.conn)
            cols = [f"{'*' if row['pk'] == '1' else ''}{row['name']} ({row['type']})" for index, row in colsDF.iterrows()]
            for col in cols:
                self.tables_tree.insert(cur, 'end', text=col)
                
        self.status.set("Database tables updated.")
    
    def disconnect(self):
        if self.connected:
            self.status.set("Disconnicting from current connection")
            self.conn.commit()
            self.conn.close()
            self.connected = False
            self.status.set("Disconniced.")
        
    def run_query(self):
        try:
            start_time = time.time()
            
            self.status.set("Running Query...")
            self.root.update()
            
            self.clear_output()
            self.df = pd.DataFrame()
            
            cur = self.conn.cursor()
            cur.execute(self.query_text.get('1.0', tk.END))
            
            #Find what sort of statement was passed
            if cur.description!=None: #Select Statement
                self.df = pd.DataFrame(cur.fetchall(), columns = [desc[0] for desc in cur.description])
                st = f"{len(self.df)} rows were retrieved in {int(time.time()-start_time)} second/s."
            elif cur.lastrowid > 0:   #Insert statement
                st = f"{cur.rowcount} new rows were inserted in {int(time.time()-start_time)} second/s."
                self.conn.commit()
            elif cur.rowcount > -1:   #update or delete statements
                st = f"{cur.rowcount} rows were effected in {int(time.time()-start_time)} second/s."
                self.conn.commit()
            else:                     #all other statements
                st = f"Statement executed succesfuly in {int(time.time()-start_time)} second/s."
                self.conn.commit()
                self.update_tables_treeview() #Refresh treeview in case of create drop .. etc statement
                
            cur.close()
            
            # if its a select statement, fill the first 1000 rows in the table (treeview)
            if not self.df.empty:
                self.result_treeview["column"] = list(self.df.columns)
                self.result_treeview["show"] = "headings"
                for column in self.result_treeview["columns"]:
                    self.result_treeview.heading(column, text=column) # let the column heading = column name
            
                df_rows = self.df.head(1000).to_numpy().tolist() # turns the dataframe into a list of lists
                for row in df_rows:
                    self.result_treeview.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
                
                self.save_button['state'] = tk.NORMAL
                self.clear_button['state'] = tk.NORMAL
            
            self.status.set(st)
            
        except Exception as e:
            self.status.set('Error.')
            messagebox.showerror(title='Query error', message=e)
    
    #clears the table and set buttons to be disables
    def clear_output(self):
        if not self.df.empty:
            self.result_treeview.delete(*self.result_treeview.get_children())
            self.result_treeview["show"] = "tree"
            self.df = pd.DataFrame()
            self.save_button['state'] = tk.DISABLED
            self.clear_button['state'] = tk.DISABLED
            self.status.set('Output cleared.')
    
    #saves result table to a csv
    def save_query(self):
        if not self.df.empty:
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(),
                                          title="Select A File",
                                          initialfile  = 'Query.csv',
                                          defaultextension = '.csv')
            self.df.to_csv(filename, index=False)
            self.status.set(f'Saved to "{filename}"')
    
    #when double clicking on the tables tree view, it will insert the table or column name into the query text
    def OnDoubleClick(self, event):

        item_iid = self.tables_tree.selection()[0]
        parent_iid = self.tables_tree.parent(item_iid)
        
        if parent_iid != '': # select item is a column if it has a parent
            col = self.tables_tree.item(item_iid)['text'].replace('*', '')
            col = col[:col.find(' (')]
            if table_name_on_col_dbl_click: col = f" {self.tables_tree.item(parent_iid)['text']}.{col} "
            self.query_text.insert(tk.INSERT, f" {col} ")
        else: # else selection is a table
            self.query_text.insert(tk.INSERT, f" {self.tables_tree.item(item_iid)['text']} ")
        
        self.query_text.focus()
        
    #find what is the last word thats being typed.
    def last_word(self):
        line, last = self.query_text.index(tk.INSERT).split('.')
        first = int(last)
        while True:
            first-=1
            if first<0: break
            if self.query_text.get(f"{line}.{first}", f"{line}.{first+1}") in word_end:
                break
        return {'word': self.query_text.get(f"{line}.{first+1}", f"{line}.{last}"), 'first': f"{line}.{first+1}", 'last': f"{line}.{last}"}
    
    #highlight the last word if its a syntax, See: syntax dictionary on the top.
    #this runs on every key release which is why it fails when the user is too fast.
    #it also highlights the current line
    def highlight(self):
        
        self.query_text.tag_remove("current_line", 1.0, "end")
        self.query_text.tag_add("current_line", "insert linestart", "insert lineend+1c")
        
        
        lastword = self.last_word()
        
        for kw in syntax:
            if lastword['word'].lower() in syntax[kw]['words']:
                self.query_text.tag_add(kw, lastword['first'], lastword['last'])
            else:
                self.query_text.tag_remove(kw, lastword['first'], lastword['last'])
        
        self.query_text.tag_raise("sel")
    #disconnects data base before exiting app
    def on_close(self):
        self.disconnect()
        self.root.destroy()

ms = tk.Tk()
me = sqllite3_gui(ms)
ms.mainloop()