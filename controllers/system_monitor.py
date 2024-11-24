import psutil

class SystemMonitor:
    def get_cpu_usage(self):
        """Get CPU usage percentage."""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        """Get RAM usage."""
        memory = psutil.virtual_memory()
        return memory.percent, memory.used, memory.total

    def get_disk_usage(self):
        """Get disk usage."""
        disk = psutil.disk_usage('/')
        return disk.percent, disk.used, disk.total

    def list_processes(self):
        """List all running processes."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            processes.append(proc.info)
        return processes
